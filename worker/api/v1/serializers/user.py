import os
import random

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError, transaction
from PIL import Image
from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    avatar = serializers.ImageField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(required=False)
    birth_of_date = serializers.DateField()
    tel = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "id",
            "avatar",
            "first_name",
            "last_name",
            "email",
            "password",
            "birth_of_date",
            "tel",
        ]

    @transaction.atomic
    def create(self, validated_data):
        if "avatar" in validated_data:
            avatar = validated_data.pop("avatar")

        password = validated_data["password"]
        if not password:
            raise serializers.ValidationError("Password is required")

        validated_data["password"] = make_password(password=password)
        try:
            ModelClass = self.Meta.model
            instance = ModelClass._default_manager.create(**validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError({"detail": str(e)})

        media_root = settings.MEDIA_ROOT
        avatar_directory = os.path.join(media_root, "images", "avatars", "custom")

        if not os.path.exists(avatar_directory):
            os.makedirs(avatar_directory, exist_ok=True)

        avatar_path = os.path.join(avatar_directory, f"{str(instance.id)}.jpg")
        if "avatar" in validated_data:
            pil_image = Image.open(avatar)
        else:
            default_img_dir = os.path.join(media_root, "images", "avatars", "default")
            img_paths = os.listdir(default_img_dir)
            random_img_idx = random.randint(0, len(img_paths) - 1)
            img_path = os.path.join(default_img_dir, img_paths[random_img_idx])
            pil_image = Image.open(img_path)
            pil_image = pil_image.convert("RGB")
            pass
        pil_image.save(avatar_path, format="JPEG")

        instance.avatar = os.path.relpath(avatar_path, media_root)
        instance.save()

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "avatar":
                media_root = settings.MEDIA_ROOT
                avatar_directory = os.path.join(
                    media_root, "images", "avatars", "custom"
                )
                avatar_path = os.path.join(avatar_directory, f"{instance.id}.jpg")
                pil_image = Image.open(value)
                pil_image.save(avatar_path, format="JPEG")
                value = os.path.relpath(avatar_path, media_root)
            elif attr == "password":
                value = make_password(password=value)

            setattr(instance, attr, value)

        instance.save()

        return instance
