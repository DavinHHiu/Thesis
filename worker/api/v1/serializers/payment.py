from rest_framework import serializers

from api.models import Payment
from api.v1.serializers import OrderDetailSerializer


class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    order = OrderDetailSerializer()
    payment_method = serializers.CharField()
    status = serializers.CharField()
    total_amount = serializers.FloatField()

    class Meta:
        model = Payment
        fields = ["id", "order" "payment_method", "status", "total_amount"]
