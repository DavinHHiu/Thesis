from rest_framework import serializers

from api.models import WishList

from .product import ProductSkuSerializer
from .user import UserSerializer


class WithListSerializer(serializers.ModelSerializer):
    product = ProductSkuSerializer()
    user = UserSerializer()

    class Meta:
        model = WishList
        fields = ["product", "user"]
