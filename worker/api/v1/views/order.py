from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import OrderDetail, OrderItem
from api.v1.serializers import OrderDetailSerializer, OrderItemSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing order details.
    """

    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [AllowAny]


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing order items.
    """

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [AllowAny]
