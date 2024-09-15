import os

from django.conf import settings
from django.db import transaction
from PIL import Image
from rest_framework import serializers
from rest_framework.utils import model_meta

from api.models import Product, ProductAttribute, ProductSku

from .category import SubCategorySerializer


class ProductAttributeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    type = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = ProductAttribute
        fields = ["id", "type", "value"]


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    categories = SubCategorySerializer(many=True, required=False)
    description = serializers.CharField(required=False)
    summary = serializers.CharField(required=False)
    rating = serializers.IntegerField(required=False)

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


class ProductSkuSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    cover = serializers.ImageField(required=False)
    size = ProductAttributeSerializer()
    color = ProductAttributeSerializer()
    sku = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    product_id = serializers.SerializerMethodField()

    class Meta:
        model = ProductSku
        fields = [
            "id",
            "cover",
            "size",
            "color",
            "sku",
            "price",
            "quantity",
        ]

    def get_product_id(self, obj):
        return obj.product.id

    @transaction.atomic
    def create(self, data):
        # Get relationship object
        related_data = data.pop("data")
        categories = related_data.pop("categories")
        size = related_data.pop("size")
        color = related_data.pop("color")

        # Get product's cover
        if "cover" in data:
            cover = data.pop("cover")

        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(size=size, color=color, **data)
        instance.categories.add(categories)

        media_root = settings.MEDIA_ROOT
        cover_directory = os.path.join(media_root, "images", "cover")
        if not os.path.exists(cover_directory):
            os.makedirs(cover_directory, exist_ok=True)

        cover_path = os.path.join(cover_directory, f"{instance.id}.jpg")
        pil_image = Image.open(cover)
        pil_image = pil_image.convert("RGB")
        pil_image.save(cover_path, format="JPEG")

        instance.cover = os.path.relpath(cover_path, media_root)

        instance.save()

        return instance

    def update(self, instance, data):
        related_data = data.pop("data")
        categories = related_data.pop("categories")
        size = related_data.pop("size")
        color = related_data.pop("color")
        if "cover" in related_data:
            cover = related_data.pop("cover")
            if isinstance(cover, str):
                media_root = settings.MEDIA_ROOT
                cover_directory = os.path.join(media_root, "images", "cover")
                if not os.path.exists(cover_directory):
                    os.makedirs(cover_directory, exist_ok=True)
                cover_path = os.path.join(cover_directory, f"{instance.id}.jpg")
                pil_image = Image.open(cover)
                pil_image = pil_image.convert("RGB")
                pil_image.save(cover_path, format="JPEG")
                instance.cover = os.path.relpath(cover_path, media_root)

        info = model_meta.get_field_info(instance)

        for attr, value in data.items():
            if not (attr in info.relations and info.relations[attr].to_many):
                setattr(instance, attr, value)

        instance.categories.set([categories])
        instance.size = size
        instance.color = color
        instance.save()

        return instance
