from rest_framework import serializers

from api.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Category
        fields = ["name", "description"]


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = SubCategory
        fields = ["category", "name", "description"]
