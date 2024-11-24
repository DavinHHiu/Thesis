from rest_framework import serializers

from api.models import OrderDetail, OrderItem

from .payment import PaymentSerializer
from .product import ProductSerializer, ProductSkuSerializer
from .shipment import ShipmentSerializer


class OrderDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField(required=False)
    user_id = serializers.CharField(source="user.id")
    total_quantity = serializers.IntegerField()
    status = serializers.CharField()
    shipment = serializers.SerializerMethodField()
    payment = serializers.SerializerMethodField()

    class Meta:
        model = OrderDetail
        fields = [
            "id",
            "user_id",
            "total_quantity",
            "status",
            "shipment",
            "payment",
        ]

    def get_shipment(self, obj):
        return ShipmentSerializer(obj.shipment).data

    def get_payment(self, obj):
        return PaymentSerializer(obj.payment).data


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    order_id = serializers.CharField()
    product_sku = ProductSkuSerializer()
    product = serializers.SerializerMethodField()
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ["id", "order_id", "product", "product_sku", "quantity"]

    def get_product(self, obj):
        return ProductSerializer(obj.product_sku.product).data
