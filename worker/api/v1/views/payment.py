from rest_framework import viewsets

from api.models import Payment
from api.v1.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing payments.
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
