from rest_framework import serializers

from api.models import Product, ProductAttribute

from .category import SubCategorySerializer


class ProductAttributeSerializer(serializers.ModelSerializer):
    type = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = ProductAttribute
        fields = ["type", "value"]


class ProductSerializer(serializers.ModelSerializer):
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
