from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Payment
from api.v1.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing payments.
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]
