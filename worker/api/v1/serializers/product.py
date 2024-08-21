from rest_framework import serializers

from api.models import Product
from api.v1.serializers import SubCategorySerializer


class ProductAttributeSerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    value = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()
    summary = serializers.CharField()
    cover = serializers.ImageField()
    categories = SubCategorySerializer()
    size = ProductAttributeSerializer()
    color = ProductAttributeSerializer()
    sku = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "summary",
            "cover",
            "categories",
            "size",
            "color",
            "sku",
            "price",
            "quantity",
        ]
