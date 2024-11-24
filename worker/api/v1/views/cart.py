from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Cart, CartItem
from api.v1.serializers import (
    CartItemSerializer,
    CartSerializer,
    ShallowCartItemSerializer,
)


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing carts.
    """

    queryset = Cart.objects.select_related("user")
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["GET"], url_path="by-user")
    def retrieveByUser(self, request, *args, **kwargs):
        try:
            cart = self.get_queryset().get(user=request.user)
            serializer = self.get_serializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            msg = _("Cart not found")
            return Response({"error": msg}, status=status.HTTP_404_NOT_FOUND)


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing cart items.
    """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ["create", "update", "destroy"]:
            return ShallowCartItemSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None, *args, **kwargs):
        cart_item = self.get_object()
        serializer = self.get_serializer(cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, *args, **kwargs):
        cart_item = self.get_object()
        cart_item.cart.total_quantity -= cart_item.quantity
        cart_item.cart.total_amount -= cart_item.subtotal
        cart_item.cart.save()
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["POST"], url_path="validate/checkout-items")
    def validateCheckoutItems(self, request, *args, **kwargs):
        checkout_items = request.data["checkout_items"]
        checkout_item_ids = [x["id"] for x in checkout_items]
        cart_items = CartItem.objects.filter(id__in=checkout_item_ids)

        serializer = self.get_serializer(cart_items, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
