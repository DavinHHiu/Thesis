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
    id = serializers.IntegerField(read_only=True, required=False)
    category = CategorySerializer()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = SubCategory
        fields = ["id", "category", "name", "description"]

    def create(self, validated_data):
        category_data = validated_data.pop("category")
        category = Category.objects.get(**category_data)
        subcategory = SubCategory.objects.create(category=category, **validated_data)
        return subcategory
