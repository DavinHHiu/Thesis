import os

from django.db import transaction
from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Product, ProductAttribute, ProductImage, ProductSku, SubCategory
from api.v1.serializers import (
    ProductAttributeSerializer,
    ProductImageSerializer,
    ProductSerializer,
    ProductSkuSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductSkuViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """

    queryset = ProductSku.objects.all()
    serializer_class = ProductSkuSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, pk=None, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing product attributes.
    """

    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = [AllowAny]


class ProductImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing product images.
    """

    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        images = request.FILES.getlist("images")
        product_sku_id = request.data.get("product_sku_id")

        if not product_sku_id:
            return Response(
                {"error": "Product SKU ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            product_sku = ProductSku.objects.get(pk=product_sku_id)
            old_images = ProductImage.objects.filter(product_sku=product_sku)
            for old_image in old_images:
                os.remove(old_image.image.path)
            old_images.delete()
        except ProductSku.DoesNotExist:
            msg = _("Product SKU does not exist")
            return Response(
                {"error": msg},
                status=status.HTTP_400_BAD_REQUEST,
            )

        data = [{"image": image, "product_sku_id": product_sku_id} for image in images]

        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        product_sku_id = request.query_params.get("product_sku_id")

        if not product_sku_id:
            return Response(
                {"error": "Product SKU ID is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            product_sku = ProductSku.objects.get(pk=product_sku_id)
        except ProductSku.DoesNotExist:
            msg = _("Product SKU does not exist")
            return Response(
                {"error": msg},
                status=status.HTTP_400_BAD_REQUEST,
            )

        images = ProductImage.objects.filter(product_sku=product_sku)

        serializer = self.get_serializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
