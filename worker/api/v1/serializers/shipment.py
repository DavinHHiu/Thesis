from rest_framework import serializers

from api.models import Shipment
from api.v1.serializers import OrderDetailSerializer


class ShipmentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    order = OrderDetailSerializer()
    shipping_method = serializers.CharField()
    shipping_fee = serializers.FloatField()
    status = serializers.CharField()

    class Meta:
        model = Shipment
        fields = ["id", "order", "shipping_method", "shipping_fee", "status"]
