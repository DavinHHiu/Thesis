from rest_framework import viewsets

from api.models import WishList
from api.v1.serializers import WithListSerializer


class WishListViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing wishlists.
    """

    queryset = WishList.objects.all()
    serializer_class = WithListSerializer
