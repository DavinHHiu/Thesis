from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import Payment, PaymentMethod
from api.v1.serializers import PaymentMethodSerializer, PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing payments.
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing payment methods.
    """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [AllowAny]
