from rest_framework import viewsets

from api.models import Shipment
from api.v1.serializers import ShipmentSerializer


class ShipmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing shipments.
    """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
