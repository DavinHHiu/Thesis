from rest_framework import serializers

from api.models import OrderDetail, OrderItem

from .product import ProductSerializer
from .user import UserSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    total = serializers.FloatField()
    status = serializers.CharField()

    class Meta:
        model = OrderDetail
        fields = ["user", "total", "status"]


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer()
    product = ProductSerializer()
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ["order", "product", "quantity"]
