from rest_framework import serializers

from api.models import WishList
from api.v1.serializers import ProductSerializer, UserSerializer


class WithListSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = WishList
        fields = ["id", "product", "user"]
