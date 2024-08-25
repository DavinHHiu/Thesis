from rest_framework import serializers

from api.models import Payment

from .order import OrderDetailSerializer


class PaymentSerializer(serializers.ModelSerializer):
    order = OrderDetailSerializer()
    payment_method = serializers.CharField()
    status = serializers.CharField()
    total_amount = serializers.FloatField()

    class Meta:
        model = Payment
        fields = ["order" "payment_method", "status", "total_amount"]
