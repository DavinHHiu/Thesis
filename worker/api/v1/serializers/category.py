from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.utils import model_meta

from api.models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Category
        fields = ["id", "name", "description"]


5


class SubCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField(source="category.id")
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = SubCategory
        fields = ["id", "category_id", "name", "description"]

    def create(self, validated_data):
        try:
            category = Category.objects.get(
                pk=validated_data.pop("category", None).get("id", None)
            )
        except Category.DoesNotExist:
            msg = _("Category does not exist")
            raise serializers.ValidationError(msg)
        validated_data["category"] = category
        return super().create(validated_data)

    def update(self, instance, validated_data):
        try:
            category = Category.objects.get(
                pk=validated_data.pop("category", None).get("id", None)
            )
        except Category.DoesNotExist:
            msg = _("Category does not exist")
            raise serializers.ValidationError(msg)
        validated_data["category"] = category

        return super().update(instance, validated_data)
