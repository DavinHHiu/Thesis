from rest_framework import serializers

from api.models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    user = serializers.SerializerMethodField()
    total = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = ["id", "user", "total"]

    def get_user(self, obj):
        from api.v1.serializers import UserSerializer

        return UserSerializer(obj.user).data


class CartItemSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    cart = CartSerializer()
    product = serializers.SerializerMethodField()
    quantity = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "quantity"]

    def get_product(self, obj):
        from api.v1.serializers import ProductSerializer

        return ProductSerializer(obj.product).data
