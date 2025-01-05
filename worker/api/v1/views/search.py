import numpy as np
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Product
from api.utils.ai_model import extract_features
from api.utils.faiss import load_index
from api.v1.serializers import (
    ProductShallowSerializer,
    SearchSerializer,
)


class SearchByImageApiView(APIView):
    """
    API view for searching by images
    """

    permission_classes = [AllowAny]
    serializer_class = SearchSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        query = serializer.validated_data["query"]
        min_price = serializer.validated_data["filter_price"].get("min")
        max_price = serializer.validated_data["filter_price"].get("max")
        features = extract_features(query)

        faiss_index = load_index(512)
        _, indices = faiss_index.search(np.array([features]), k=100)

        product_ids = list(
            dict.fromkeys(faiss_index.product_ids[i] for i in indices[0])
        )

        products = list(
            Product.objects.filter(
                id__in=product_ids,
                skus__price__gte=min_price,
                skus__price__lte=max_price,
            ).distinct()
        )

        sorted_products = sorted(products, key=lambda p: product_ids.index(p.id.hex))

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(sorted_products, request)

        serializer = ProductShallowSerializer(
            paginated_products, many=True, context={"request": request}
        )

        return paginator.get_paginated_response(serializer.data)


class SearchByTextApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = SearchSerializer
    pagination_class = LimitOffsetPagination

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        query = serializer.validated_data["query"]
        min_price = serializer.validated_data["filter_price"].get("min")
        max_price = serializer.validated_data["filter_price"].get("max")
        products = (
            Product.objects.filter(
                name__icontains=query,
                skus__price__gte=min_price,
                skus__price__lte=max_price,
            )
            .distinct()
            .order_by("name")
        )

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)

        serializer = ProductShallowSerializer(
            paginated_products, many=True, context={"request": request}
        )

        return paginator.get_paginated_response(serializer.data)
