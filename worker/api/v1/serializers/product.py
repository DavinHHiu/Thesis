import os

from django.conf import settings
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from PIL import Image
from rest_framework import serializers
from rest_framework.utils import model_meta

from api.models import Product, ProductAttribute, ProductImage, ProductSku, SubCategory
from api.utils.ai_model import extract_features
from api.utils.faiss import add_to_index, load_index

from .category import SubCategorySerializer
from .mixin import CreateAndUpdateSerializer


class ProductAttributeSerializer(CreateAndUpdateSerializer):
    id = serializers.IntegerField(required=False)
    type = serializers.CharField()
    value = serializers.CharField()

    class Meta:
        model = ProductAttribute
        fields = ["id", "type", "value"]


class ProductSerializer(CreateAndUpdateSerializer):
    id = serializers.UUIDField(required=False)
    name = serializers.CharField(required=False)
    categories = SubCategorySerializer(many=True, required=False)
    description = serializers.CharField(required=False)
    summary = serializers.CharField(required=False, allow_null=True)
    rating = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = "__all__"

    @transaction.atomic
    def create(self, data):
        categories = data.pop("categories")
        sub_category = SubCategory.objects.get(pk=categories[0].get("id"))

        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(**data)
        instance.categories.set([sub_category])
        instance.save()

        return instance

    @transaction.atomic
    def update(self, instance, data):
        categories = data.pop("categories")
        sub_category = SubCategory.objects.get(pk=categories[0].get("id"))

        info = model_meta.get_field_info(instance)

        for attr, value in data.items():
            if not (attr in info.relations and info.relations[attr].to_many):
                setattr(instance, attr, value)

        instance.categories.set([sub_category])
        instance.save()

        return instance


class ProductSkuSerializer(CreateAndUpdateSerializer):
    id = serializers.UUIDField(required=False)
    size = ProductAttributeSerializer()
    color = ProductAttributeSerializer()
    sku = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    product_id = serializers.CharField(allow_null=True)

    class Meta:
        model = ProductSku
        fields = [
            "id",
            "size",
            "color",
            "sku",
            "price",
            "quantity",
            "product_id",
        ]

    @transaction.atomic
    def create(self, data):
        size_data = data.pop("size")
        color_data = data.pop("color")
        product_id = data.pop("product_id")

        if not size_data or not color_data or not product_id:
            msg = _("Missing required fields")
            raise serializers.ValidationError(msg)

        try:
            size = ProductAttribute.objects.get(pk=size_data["id"])
            color = ProductAttribute.objects.get(pk=color_data["id"])
            product = Product.objects.get(pk=product_id)
        except ProductAttribute.DoesNotExist:
            msg = _("Product attribute does not exist")
            raise serializers.ValidationError(msg)
        except Product.DoesNotExist:
            msg = _("Product does not exist")
            raise serializers.ValidationError(msg)

        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(
            product=product, size=size, color=color, **data
        )

        return instance

    def update(self, instance, data):
        size_data = data.pop("size")
        color_data = data.pop("color")
        product_id = data.pop("product_id")

        if not size_data or not color_data or not product_id:
            msg = _("Missing required fields")
            raise serializers.ValidationError(msg)

        try:
            size = ProductAttribute.objects.get(pk=size_data["id"])
            color = ProductAttribute.objects.get(pk=color_data["id"])
            product = Product.objects.get(pk=product_id)
        except (ProductAttribute.DoesNotExist, Product.DoesNotExist):
            raise serializers.ValidationError(_("Invalid product attribute or product"))

        data["size"] = size
        data["color"] = color
        data["product"] = product

        info = model_meta.get_field_info(instance)

        for attr, value in data.items():
            if not (attr in info.relations and info.relations[attr].to_many):
                setattr(instance, attr, value)

        instance.save()

        return instance


class ProductImageSerializer(CreateAndUpdateSerializer):
    id = serializers.IntegerField(required=False)
    image = serializers.ImageField()
    product_sku_id = serializers.CharField()

    class Meta:
        model = ProductImage
        fields = ["id", "image", "product_sku_id"]

    @transaction.atomic
    def create(self, data):
        product_sku_id = data.pop("product_sku_id")
        image_data = data.pop("image")

        try:
            product_sku = ProductSku.objects.get(pk=product_sku_id)
        except ProductSku.DoesNotExist:
            msg = _("Product SKU does not exist")
            raise serializers.ValidationError(msg)

        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(product_sku=product_sku)

        media_root = settings.MEDIA_ROOT
        image_dir = os.path.join(
            media_root,
            "images",
            "product",
            product_sku_id,
        )
        os.makedirs(image_dir, exist_ok=True)
        image_path = os.path.join(image_dir, f"{instance.id }.jpg")

        image = Image.open(image_data)
        image = image.convert("RGB")
        image.save(image_path, format="JPEG")

        instance.image = os.path.relpath(image_path, media_root)

        feature = extract_features(image_data)
        feature_str = ",".join(map(str, feature))
        instance.feature = feature_str

        faiss_index = load_index(512)
        add_to_index(faiss_index, feature, product_sku.product.id)

        instance.save()

        return instance


class ProductImageDisplaySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()

    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductSkuDisplaySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    size = ProductAttributeSerializer()
    color = ProductAttributeSerializer()
    sku = serializers.CharField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    images = ProductImageDisplaySerializer(required=False, allow_null=True, many=True)
    product = ProductSerializer()

    class Meta:
        model = ProductSku
        fields = "__all__"


class ProductDisplaySerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    categories = SubCategorySerializer(many=True)
    description = serializers.CharField()
    summary = serializers.CharField()
    rating = serializers.IntegerField()
    skus = ProductSkuDisplaySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductShallowSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    rating = serializers.IntegerField()
    images = serializers.SerializerMethodField()
    colors = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    prices = serializers.SerializerMethodField()

    def get_images(self, obj):
        first_sku = obj.skus.first()
        request = self.context.get("request", None)
        if first_sku:
            product_images = first_sku.images.all()
            return [
                request.build_absolute_uri(product_image.image.url)
                for product_image in product_images
            ]
        return []

    def get_categories(self, obj):
        return obj.categories.values_list("name", flat=True)

    def get_prices(self, obj):
        return obj.skus.values_list("price", flat=True)

    def get_colors(self, obj):
        return obj.skus.values_list("color__value", flat=True).distinct()


class ProductSkuDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    size = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    price = serializers.FloatField()
    quantity = serializers.IntegerField()
    images = serializers.SerializerMethodField()

    def get_size(self, obj):
        return obj.size.value

    def get_color(self, obj):
        return obj.color.value

    def get_images(self, obj):
        image_paths = obj.images.values_list("image", flat=True)
        return [self._build_image_uri(image) for image in image_paths]

    def _build_image_uri(self, relative_uri):
        return settings.BASE_MEDIA_URL + relative_uri.replace("\\", "/")


class ProductDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    rating = serializers.IntegerField()
    description = serializers.CharField()
    summary = serializers.CharField()
    categories = serializers.SerializerMethodField()
    skus = ProductSkuDetailSerializer(many=True)

    def get_prices(self, obj):
        return obj.skus.values_list("price", flat=True)

    def get_categories(self, obj):
        return obj.categories.values_list("name", flat=True)
