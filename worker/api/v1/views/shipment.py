from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Shipment, ShipmentMethod
from api.v1.serializers import ShipmentMethodSerializer, ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing shipments.
    """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    permission_classes = [AllowAny]


class ShipmentMethodViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing shipment methods.
    """

    queryset = ShipmentMethod.objects.all()
    serializer_class = ShipmentMethodSerializer
    permission_classes = [AllowAny]
