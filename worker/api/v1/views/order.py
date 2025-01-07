import paypalrestsdk
from django.conf import settings
from django.db import transaction
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _
from paypalrestsdk import Payment as PaypalPayment
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.consts import base_consts
from api.models import (
    Address,
    CartItem,
    OrderDetail,
    OrderItem,
    Payment,
    PaymentMethod,
    Shipment,
    ShipmentMethod,
)
from api.v1.serializers import OrderDetailSerializer, OrderItemSerializer


class OrderDetailPagination(LimitOffsetPagination):

    def get_paginated_response(self, data):
        OrderDetailViewSet = import_string("api.v1.views.order.OrderDetailViewSet")
        queryset = OrderDetailViewSet.queryset
        return Response(
            {
                "count": self.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "results": data,
                "counter": {
                    "pending": queryset.filter(
                        status=base_consts.ORDER_STATUS_PENDING
                    ).count(),
                    "confirmed": queryset.filter(
                        status=base_consts.ORDER_STATUS_COMFIRMED
                    ).count(),
                    "processing": queryset.filter(
                        status=base_consts.ORDER_STATUS_PROCESSING
                    ).count(),
                    "shipping": queryset.filter(
                        status=base_consts.ORDER_STATUS_SHIPPING
                    ).count(),
                    "delivered": queryset.filter(
                        status=base_consts.ORDER_STATUS_DELIVERED
                    ).count(),
                    "completed": queryset.filter(
                        status=base_consts.ORDER_STATUS_COMPLETED
                    ).count(),
                    "cancelled": queryset.filter(
                        status=base_consts.ORDER_STATUS_CANCELLED
                    ).count(),
                    "refunded": queryset.filter(
                        status=base_consts.ORDER_STATUS_REFUNDED
                    ).count(),
                },
            }
        )


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing order details.
    """

    permission_classes = [AllowAny]
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    pagination_class = OrderDetailPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        order_status = self.request.query_params.get("status")
        if order_status:
            queryset = queryset.filter(status=order_status)
        return queryset


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing order items.
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [AllowAny]

    @transaction.atomic
    def create(self, request):
        order_id = request.data.get("order_id")

        try:
            order = OrderDetail.objects.get(id=order_id)
        except OrderDetail.DoesNotExist:
            msg = _("Order does not exist")
            return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        checkout_items = request.data.get("checkout_items")
        checkout_item_ids = [i.get("id") for i in checkout_items]
        cart_items = CartItem.objects.select_related("cart", "product_sku").filter(
            id__in=checkout_item_ids
        )

        total_quantity = 0
        total_amount = 0
        order_items = []
        for item in cart_items:
            order_items.append(
                OrderItem(
                    order=order,
                    product_sku=item.product_sku,
                    quantity=item.quantity,
                    subtotal=item.subtotal,
                )
            )

            total_quantity += item.quantity
            total_amount += item.subtotal

        OrderItem.objects.bulk_create(order_items)
        cart = cart_items[0].cart
        cart.total_quantity -= total_quantity
        cart.total_amount -= total_amount
        cart.save()
        cart_items.delete()

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="by-order/(?P<order_id>[^/.]+)")
    def retrieveByOrder(self, request, order_id=None, *args, **kwargs):
        if order_id:
            order_items = OrderItem.objects.filter(order_id=order_id)
            serializer = self.get_serializer(order_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


def configure_paypal():
    paypalrestsdk.configure(
        {
            "mode": settings.PAYPAL_ENVIRONMENT,
            "client_id": settings.PAYPAL_CLIENT_ID,
            "client_secret": settings.PAYPAL_CLIENT_SECRET,
        }
    )


class CreatePaymentView(APIView):
    permission_classes = [AllowAny]

    def _request_order(self, total_amount, host):
        configure_paypal()
        payment = paypalrestsdk.Payment(
            {
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "transactions": [
                    {
                        "amount": {
                            "currency": "USD",
                            "total": f"{total_amount:.2f}",
                        },
                    }
                ],
                "redirect_urls": {
                    "return_url": f"{host}/payment-success",
                    "cancel_url": f"{host}/payment-cancel",
                },
            }
        )

        return payment

    @transaction.atomic
    def post(self, request):
        address_data = request.data.get("address")
        shipment_method = request.data.get("shipment_method")
        payment_method = request.data.get("payment_method")
        total_amount = request.data.get("total_amount")
        total_quantity = request.data.get("total_quantity")
        host = request.data.get("host")

        if not address_data:
            msg = _("You need to fill in the address to place the order")
            return Response({"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        order_address, created = Address.objects.get_or_create(
            user=request.user, **address_data
        )
        if not created:
            order_address.pk = None
            order_address.save()

        payment_status = base_consts.PAYMENT_STATUS_PENDING
        response_status = status.HTTP_200_OK
        response = {}

        if payment_method.get("value") == base_consts.PAYMENT_METHOD_COD:
            order_status = base_consts.ORDER_STATUS_COMFIRMED
        else:
            order_status = base_consts.ORDER_STATUS_PENDING

            payment = self._request_order(total_amount, host)
            if payment.create():
                order_status = base_consts.ORDER_STATUS_COMFIRMED
                payment_status = base_consts.PAYMENT_STATUS_SUCCESS
                for link in payment.links:
                    if link.rel == "approval_url":
                        response = {
                            "approval_url": link.href,
                        }
            else:
                msg = _("Could not create payment")
                response = {"error": msg}
                response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
                payment_status = base_consts.PAYMENT_STATUS_FAIL

        order = OrderDetail.objects.create(
            user=request.user,
            total_quantity=total_quantity,
            status=order_status,
        )
        response["order_id"] = order.id

        try:
            db_shipment_method = ShipmentMethod.objects.get(
                id=shipment_method.get("id")
            )
            Shipment.objects.create(
                order=order,
                receive_address=order_address,
                shipment_method=db_shipment_method,
            )
        except ShipmentMethod.DoesNotExist:
            msg = _("Shipping method does not exist")
            return Response({"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        try:
            db_payment_method = PaymentMethod.objects.get(id=payment_method.get("id"))
            Payment.objects.create(
                id=payment.id,
                order=order,
                payment_method=db_payment_method,
                total_amount=total_amount,
                status=payment_status,
            )
        except PaymentMethod.DoesNotExist:
            msg = _("Payment method does not exist")
            return Response({"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=response_status)


class ExecutePaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        token = data.get("token")
        payer_id = data.get("PayerID")
        payment_id = data.get("paymentId")

        if token and payer_id:
            configure_paypal()

            payment = PaypalPayment.find(payment_id)

            if payment.state == "created":
                execute_payment = payment.execute({"payer_id": payer_id})
                if execute_payment:
                    try:
                        payment = Payment.objects.get(id=payment_id)
                        return Response(
                            {"order_id": payment.order.id}, status=status.HTTP_200_OK
                        )
                    except Payment.DoesNotExist:
                        msg = _("Payment does not exist")
                        return Response(
                            {"detail": msg}, status=status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {"error": "Payment execution failed."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"error": "Payment was not approved."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            {"error": "Invalid token or payer ID"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
