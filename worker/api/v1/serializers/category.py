from rest_framework import serializers

from api.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    category = CategorySerializer()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = SubCategory
        fields = ["id", "category", "name", "description"]
