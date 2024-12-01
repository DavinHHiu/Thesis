from datetime import datetime, timedelta

from django.db.models import Sum
from django.db.models.functions import TruncDay
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Payment, PaymentMethod
from api.v1.serializers import (
    PaymentMethodSerializer,
    PaymentSerializer,
    RevenueStatisticsSerializer,
)


class PaymentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing payments.
    """

    queryset = Payment.objects.select_related("payment_method").all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]


class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing payment methods.
    """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = [AllowAny]


class RevenueStatisticsApiView(APIView):
    """
    API endpoint for retrieving revenue statistics.
    """

    queryset = Payment.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = RevenueStatisticsSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        converted_data = {
            "start_date": datetime.fromisoformat(request.data.get("start_date", None)),
            "end_date": datetime.fromisoformat(request.data.get("end_date", None)),
        }
        serializer = self.serializer_class(data=converted_data)
        serializer.is_valid(raise_exception=True)

        start_date = serializer.validated_data["start_date"]
        end_date = serializer.validated_data["end_date"]

        queryset = self.queryset.filter(
            created_at__gte=start_date, created_at__lte=end_date
        )
        revenue_stattistics = (
            queryset.annotate(day=TruncDay("created_at"))
            .values("day")
            .annotate(total_amount=Sum("total_amount"))
            .order_by("day")
        )

        response = {}
        cur_date = start_date
        while cur_date <= end_date:
            response[cur_date.isoformat()] = 0
            cur_date += timedelta(days=1)

        for entry in revenue_stattistics:
            response[entry["day"].isoformat()] = entry["total_amount"]

        return Response(response, status=status.HTTP_200_OK)
