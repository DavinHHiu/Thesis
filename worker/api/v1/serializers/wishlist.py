from rest_framework import serializers

from api.models import WishList

from .mixin import CreateAndUpdateSerializer
from .product import ProductSkuSerializer
from .user import UserSerializer


class WithListSerializer(CreateAndUpdateSerializer):
    product = ProductSkuSerializer()
    user = UserSerializer()

    class Meta:
        model = WishList
        fields = ["product", "user"]
