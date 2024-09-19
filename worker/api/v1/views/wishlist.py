from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import WishList
from api.v1.serializers import WithListSerializer


class WishListViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing wishlists.
    """

    queryset = WishList.objects.all()
    serializer_class = WithListSerializer
    permission_classes = [AllowAny]
