from rest_framework import serializers

from api.models import District, Province, Ward

from .mixin import CreateAndUpdateSerializer


class ProvinceSerializer(CreateAndUpdateSerializer):
    code = serializers.IntegerField()
    name = serializers.CharField()
    division_type = serializers.CharField()
    codename = serializers.CharField()
    phone_code = serializers.IntegerField()
    is_active = serializers.BooleanField()

    class Meta:
        model = Province
        fields = "__all__"


class DistrictSerializer(CreateAndUpdateSerializer):
    code = serializers.IntegerField()
    name = serializers.CharField()
    division_type = serializers.CharField()
    codename = serializers.CharField()
    province_code = serializers.IntegerField(source="province.code")
    is_active = serializers.BooleanField()

    class Meta:
        model = District
        fields = [
            "code",
            "name",
            "division_type",
            "codename",
            "province_code",
            "is_active",
        ]


class WardSerializer(CreateAndUpdateSerializer):
    code = serializers.IntegerField()
    name = serializers.CharField()
    division_type = serializers.CharField()
    codename = serializers.CharField()
    district_code = serializers.IntegerField(source="district.code")
    is_active = serializers.BooleanField()

    class Meta:
        model = Ward
        fields = [
            "code",
            "name",
            "division_type",
            "codename",
            "district_code",
            "is_active",
        ]
