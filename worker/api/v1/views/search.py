import numpy as np
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product
from api.utils.ai_model import extract_features
from api.utils.faiss import load_index
from api.v1.serializers import ImageSerializer, ProductShallowSerializer, TextSerializer


class SearchByImageApiView(APIView):
    """
    API view for searching by images
    """

    permission_classes = [AllowAny]
    serializer_class = ImageSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        image = serializer.validated_data["image"]
        features = extract_features(image)

        faiss_index = load_index(512)
        _, indices = faiss_index.search(np.array([features]), k=100)

        product_ids = list(
            dict.fromkeys(faiss_index.product_ids[i] for i in indices[0])
        )

        products = list(Product.objects.filter(id__in=product_ids))

        sorted_products = sorted(products, key=lambda p: product_ids.index(p.id.hex))

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(sorted_products, request)

        serializer = ProductShallowSerializer(
            paginated_products, many=True, context={"request": request}
        )

        return paginator.get_paginated_response(serializer.data)


class SearchByTextApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = TextSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        keyword = serializer.validated_data["text"]
        products = Product.objects.filter(name__icontains=keyword)

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductShallowSerializer(
            paginated_products, many=True, context={"request": request}
        )

        return paginator.get_paginated_response(serializer.data)
