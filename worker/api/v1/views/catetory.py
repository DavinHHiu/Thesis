from django.utils.translation import gettext_lazy as _
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import Category, SubCategory
from api.v1.serializers import CategorySerializer, SubCategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class SubCategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing sub categories.
    """

    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [AllowAny]

    def list(self, request):
        category_id = request.query_params.get("category_id")

        if not category_id:
            msg = _("Category ID is required")
            return Response(
                {"error": msg},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            msg = _("Category does not exist")
            return Response(
                {"error": msg},
                status=status.HTTP_400_BAD_REQUEST,
            )

        subcategories = SubCategory.objects.filter(category=category)
        serializer = self.get_serializer(subcategories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
