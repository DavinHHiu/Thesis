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

    queryset = Cart.objects.select_related("user").all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["GET"], url_path="by-user/(?P<user_id>[^/.]+)")
    def retrieveByUser(self, request, user_id=None, *args, **kwargs):
        if user_id:
            try:
                cart = self.get_queryset().get(user_id=user_id)
                serializer = self.get_serializer(cart)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Cart.DoesNotExist:
                msg = _("Cart not found for user ID")
                return Response({"error": msg}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


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
