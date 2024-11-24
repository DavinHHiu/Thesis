import uuid

from django.conf import settings
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCaptureRequest, OrdersCreateRequest
from rest_framework import status, viewsets
from rest_framework.decorators import action
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


class PayPalClient:
    def __init__(self):
        self.client_id = settings.PAYPAL_CLIENT_ID
        self.client_secret = settings.PAYPAL_CLIENT_SECRET

        # Sử dụng môi trường sandbox hoặc live
        self.environment = SandboxEnvironment(
            client_id=self.client_id, client_secret=self.client_secret
        )

        # Khởi tạo PayPalHttpClient với môi trường
        self.client = PayPalHttpClient(self.environment)


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing order details.
    """

    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [AllowAny]

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
        cart_items = CartItem.objects.select_related("product_sku").filter(
            id__in=checkout_item_ids
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product_sku=item.product_sku,
                quantity=item.quantity,
                subtotal=item.subtotal,
            )

        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="by-order/(?P<order_id>[^/.]+)")
    def retrieveByOrder(self, request, order_id=None, *args, **kwargs):
        if order_id:
            order_items = OrderItem.objects.filter(order_id=order_id)
            serializer = self.get_serializer(order_items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CreatePaymentView(APIView):
    permission_classes = [AllowAny]

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

        if payment_method.get("value") == base_consts.PAYMENT_METHOD_COD:
            order_status = base_consts.ORDER_STATUS_COMFIRMED
            order_id = str(uuid.uuid4())
            response = {"order_id": order_id}
        else:
            order_status = base_consts.ORDER_STATUS_PENDING

            paypal_client = PayPalClient()

            request_order = OrdersCreateRequest()
            request_order.prefer("return=representation")
            request_order.request_body(
                {
                    "intent": "CAPTURE",
                    "purchase_units": [
                        {
                            "amount": {
                                "currency_code": "USD",
                                "value": f"{total_amount:.2f}",
                            },
                        }
                    ],
                    "application_context": {
                        "return_url": f"{host}/payment-success",
                        "cancel_url": f"{host}/payment-cancel",
                    },
                }
            )

            response = paypal_client.client.execute(request_order)

            if response.status_code == status.HTTP_201_CREATED:
                order_id = response.result.id
                for link in response.result.links:
                    if link.rel == "approve":
                        response = {
                            "approval_url": link.href,
                            "order_id": order_id,
                        }
            else:
                return Response(
                    {"error": "Could not create payment"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        order = OrderDetail.objects.create(
            id=order_id,
            user=request.user,
            total_quantity=total_quantity,
            status=order_status,
        )

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
                order=order,
                payment_method=db_payment_method,
                total_amount=total_amount,
            )
        except PaymentMethod.DoesNotExist:
            msg = _("Payment method does not exist")
            return Response({"detail": msg}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_200_OK)


class ExecutePaymentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        token = data.get("token")
        payer_id = data.get("PayerID")

        if token and payer_id:
            paypal_client = PayPalClient()

            # Tìm và thực hiện thanh toán bằng cách xác nhận order_id
            capture_request = OrdersCaptureRequest(token)
            capture_request.request_body({"payer_id": payer_id})
            response = paypal_client.client.execute(capture_request)

            if response.status_code == 201 and response.result.status == "COMPLETED":
                # Xử lý logic sau khi thanh toán thành công (ví dụ: cập nhật đơn hàng)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Could not capture payment"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
