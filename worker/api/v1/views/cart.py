from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Cart, CartItem, User
from api.v1.serializers import CartItemSerializer, CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing carts.
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing cart items.
    """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["GET"], url_path="list-by-cart")
    def listByCart(self, request, *arg, **kwargs):
        cart_id = request.query_params.get("cart_id")

        try:
            cart = Cart.objects.get(pk=cart_id)
        except Cart.DoesNotExist:
            msg = _("Cart does not exist")
            return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = CartItem.objects.filter(cart=cart)
        serializer = self.get_serializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="list-by-user")
    def listByUser(self, request, *arg, **kwargs):
        user_id = request.query_params.get("user_id")
        user = User.objects.get(pk=user_id)

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            msg = _("Cart does not exist")
            return Response({"error": msg}, status=status.HTTP_400_BAD_REQUEST)

        cart_items = CartItem.objects.filter(cart=cart)
        serializer = self.get_serializer(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
