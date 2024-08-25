from rest_framework import serializers

from api.models import Cart, CartItem

from .product import ProductSerializer
from .user import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    total = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ["user", "total"]


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ["cart", "product", "quantity"]