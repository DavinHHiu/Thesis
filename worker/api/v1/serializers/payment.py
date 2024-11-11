from rest_framework import serializers

from api.models import Payment, PaymentMethod


class PaymentMethodSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    icon = serializers.ImageField(required=False)
    name = serializers.CharField()
    value = serializers.CharField()
    description = serializers.CharField()
    is_active = serializers.BooleanField(required=False)

    class Meta:
        model = PaymentMethod
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    payment_method = PaymentMethodSerializer()
    total_amount = serializers.FloatField()

    class Meta:
        model = Payment
        fields = [
            "id",
            "payment_method",
            "total_amount",
        ]
