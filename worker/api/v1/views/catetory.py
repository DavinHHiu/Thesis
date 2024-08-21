from rest_framework import viewsets

from api.models import Category, SubCategory
from api.v1.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing sub categories.
    """

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
