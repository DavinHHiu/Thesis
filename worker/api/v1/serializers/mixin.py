from rest_framework import serializers


class CreateAndUpdateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)
