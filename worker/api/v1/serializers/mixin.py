from rest_framework import serializers


class CreateAndUpdateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class TextSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, allow_blank=True)


class FilterPriceSerializer(serializers.Serializer):
    min = serializers.IntegerField()
    max = serializers.IntegerField()


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField(allow_blank=True)
    filter_price = FilterPriceSerializer()
