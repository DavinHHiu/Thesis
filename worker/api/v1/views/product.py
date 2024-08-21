from rest_framework import viewsets

from api.models import Product, ProductAttribute
from api.v1.serializers import ProductAttributeSerializer, ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing products.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductAttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing product attributes.
    """

    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
