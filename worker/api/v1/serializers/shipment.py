from rest_framework import serializers

from api.models import Shipment, ShipmentMethod

from .user import AddressSerializer


class ShipmentMethodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    value = serializers.CharField()
    description = serializers.CharField()
    estimated_shipping_days = serializers.IntegerField()
    shipping_fee = serializers.FloatField()
    is_active = serializers.BooleanField(required=False)

    class Meta:
        model = ShipmentMethod
        fields = "__all__"


class ShipmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    receive_address = AddressSerializer()
    shipment_method = ShipmentMethodSerializer()
    shipping_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Shipment
        fields = [
            "id",
            "receive_address",
            "shipment_method",
            "shipping_date",
        ]
