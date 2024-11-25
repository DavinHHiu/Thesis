from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.models import District, Province, Ward
from api.v1.serializers import DistrictSerializer, ProvinceSerializer, WardSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing provinces.
    """

    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    permission_classes = [AllowAny]


class DistrictViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing districts.
    """

    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [AllowAny]

    @action(
        detail=False, methods=["GET"], url_path="by-province/(?P<province_code>\d+)"
    )
    def list_by_provice(self, request, province_code: int = None, **kwargs):
        if province_code:
            districts = self.get_queryset().filter(province__code=province_code)
            serializer = self.get_serializer(districts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class WardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing wards.
    """

    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    permission_classes = [AllowAny]

    @action(
        detail=False, methods=["GET"], url_path="by-district/(?P<district_code>\d+)"
    )
    def list_by_district(self, request, district_code: int = None, **kwargs):
        if district_code:
            wards = self.get_queryset().filter(district__code=district_code)
            serializer = self.get_serializer(wards, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
