from rest_framework import serializers

from api.models import OrderDetail, OrderItem


class OrderDetailSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    user = serializers.SerializerMethodField()
    total = serializers.FloatField()
    status = serializers.CharField()

    class Meta:
        model = OrderDetail
        fields = ["id", "user", "total", "status"]

    def get_user(self, obj):
        from api.v1.serializers import UserSerializer

        return UserSerializer(obj.user).data


class OrderItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    order = OrderDetailSerializer()
    product = serializers.SerializerMethodField()
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ["id", "order", "product", "quantity"]

    def get_product(self, obj):
        from api.v1.serializers import ProductSerializer

        return ProductSerializer(obj.product).data
