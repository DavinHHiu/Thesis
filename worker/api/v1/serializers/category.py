from rest_framework import serializers

from api.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(source="category.id")
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = SubCategory
        fields = ["id", "category_id", "name", "description"]

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category = Category.objects.get(**category_data)
        subcategory = SubCategory.objects.create(category=category, **validated_data)
        return subcategory
