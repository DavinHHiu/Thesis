from django.db import transaction
from rest_framework import status, viewsets
from rest_framework.response import Response

from api.models import Product, ProductAttribute, SubCategory
from api.v1.serializers import ProductAttributeSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @transaction.atomic
    def create(self, request):
        data = request.data.copy()
        related_data = {}

        if "color[id]" in data:
            color_id = data["color[id]"]
            color = ProductAttribute.objects.get(pk=color_id)
            related_data["color"] = color
        if "size[id]" in data:
            size_id = data["size[id]"]
            size = ProductAttribute.objects.get(pk=size_id)
            related_data["size"] = size
        if "categories[id]" in data:
            subcategory_id = data["categories[id]"]
            subcategory = SubCategory.objects.get(pk=subcategory_id)
            related_data["categories"] = subcategory

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(data=related_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @transaction.atomic
    def update(self, request, pk=None, *args, **kwargs):
        data = request.data.copy()
        related_data = {}

        if "color[id]" in data:
            color_id = data["color[id]"]
            color = ProductAttribute.objects.get(pk=color_id)
            related_data["color"] = color
        if "size[id]" in data:
            size_id = data["size[id]"]
            size = ProductAttribute.objects.get(pk=size_id)
            related_data["size"] = size
        if "categories[0][id]" in data:
            subcategory_id = data["categories[0][id]"]
            subcategory = SubCategory.objects.get(pk=subcategory_id)
            related_data["categories"] = subcategory
        if "cover" in data:
            related_data["cover"] = data["cover"]

        product = self.get_object()

        serializer = self.get_serializer(product, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(data=related_data)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductAttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing product attributes.
    """

    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
