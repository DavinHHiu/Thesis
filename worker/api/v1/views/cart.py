from rest_framework import viewsets

from api.models import Cart, CartItem
from api.v1.serializers import CartItemSerializer, CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing carts.
    """

    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing cart items.
    """

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
