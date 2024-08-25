from rest_framework import serializers

from api.models import Shipment

from .order import OrderDetailSerializer


class ShipmentSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer()
    shipping_method = serializers.CharField()
    shipping_fee = serializers.FloatField()
    status = serializers.CharField()

    class Meta:
        model = Shipment
        fields = ["order", "shipping_method", "shipping_fee", "status"]
