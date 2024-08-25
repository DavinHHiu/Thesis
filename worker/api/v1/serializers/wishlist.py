from rest_framework import serializers

from api.models import WishList

from .product import ProductSerializer
from .user import UserSerializer


class WithListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = UserSerializer()

    class Meta:
        model = WishList
        fields = ["product", "user"]
