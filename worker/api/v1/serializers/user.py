import calendar
import os
import random
from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from PIL import Image
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from api.authentications import JSONWebTokenAuthentication
from api.models import Address, User
from api.v1.serializers import EmailValidationSerializer

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False)
    avatar = serializers.ImageField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField()
    password = serializers.CharField(required=False)
    birth_of_date = serializers.DateField(required=False)
    tel = serializers.CharField(max_length=10, required=False)

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
    def validate(self, data):
        serializer = EmailValidationSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        existing_users = User.objects.filter(email=data["email"])
        if len(existing_users) > 0:
            msg = _("Email already exists")
            raise serializers.ValidationError(msg)
        return super().validate(data)

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


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    user = UserSerializer()
    title = serializers.CharField()
    address_1 = serializers.CharField()
    address_2 = serializers.CharField(required=False)
    zipcode = serializers.CharField(required=False)
    tel = serializers.CharField(max_length=10)

    class Meta:
        model = Address
        fields = [
            "id",
            "user",
            "title",
            "address_1",
            "address_2",
            "zipcode",
            "tel",
        ]

    @transaction.atomic
    def create(self, validated_data):
        if "user" in validated_data:
            user_data = validated_data.pop("user")
            try:
                user = User.objects.get(**user_data)
            except User.DoesNotExist as e:
                raise serializers.ValidationError({"detail": str(e)})

        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(user=user, **validated_data)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "user":
                user_data = value
                try:
                    user = User.objects.get(**user_data)
                except User.DoesNotExist as e:
                    raise serializers.ValidationError({"detail": str(e)})
                value = user
            setattr(instance, attr, value)

        instance.save()

        return instance


class BaseJSONWebTokenSerializer(serializers.Serializer):
    """JSONWebTokenSerializer"""

    def __init__(self, *args, **kwargs):
        """
        Dynamically add the USERNAME_FIELD to self.fields.
        """
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields["password"] = serializers.CharField(write_only=True)

    @property
    def username_field(self):
        return get_user_model().USERNAME_FIELD

    def validate(self, data: dict) -> dict:
        credentials = {
            self.username_field: data.get(self.username_field),
            "password": data.get("password"),
        }

        if all(credentials.values()):
            serializer = EmailValidationSerializer(
                data={"email": data.get(self.username_field)}
            )
            serializer.is_valid(raise_exception=True)

            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _("User account is disabled.")
                    raise serializers.ValidationError(msg)

                payload = JSONWebTokenAuthentication.jwt_create_payload(user)

                return {
                    "token": JSONWebTokenAuthentication.jwt_encode_payload(payload),
                    "user": user,
                    "issued_at": payload.get("iat", datetime.utcnow().isoformat()),
                }
            else:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg)
        else:
            msg = _("Must include '{username_field}' and 'password'.")
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)


class VerificationBaseSerializer(serializers.Serializer):
    """
    Abstract serializer used for verifying and refreshing JWTs.
    """

    token = serializers.CharField()

    def validate(self, attrs):
        msg = "Please define a validate method."
        raise NotImplementedError(msg)

    def _check_payload(self, token):
        # Check payload valid (based off of JSONWebTokenAuthentication,
        # may want to refactor)
        try:
            payload = JSONWebTokenAuthentication.jwt_decode_payload(token)
        except jwt.ExpiredSignature:
            msg = _("Signature has expired.")
            raise serializers.ValidationError(msg)
        except jwt.DecodeError:
            msg = _("Error decoding signature.")
            raise serializers.ValidationError(msg)

        return payload

    def _check_user(self, payload):
        username = JSONWebTokenAuthentication.jwt_get_username_from_payload(payload)

        if not username:
            msg = _("Invalid payload.")
            raise serializers.ValidationError(msg)

        # Make sure user exists
        try:
            user = User.objects.get_by_natural_key(username)
        except User.DoesNotExist:
            msg = _("User doesn't exist.")
            raise serializers.ValidationError(msg)

        if not user.is_active:
            msg = _("User account is disabled.")
            raise serializers.ValidationError(msg)

        return user


class RefreshJSONWebTokenSerializer(VerificationBaseSerializer):
    """
    Refresh an access token.
    """

    def validate(self, data):
        token = data["token"]

        payload = self._check_payload(token=token)
        user = self._check_user(payload=payload)
        # Get and check 'orig_iat'
        orig_iat = payload.get("orig_iat")

        if orig_iat:
            # Verify expiration
            refresh_limit = api_settings.JWT_REFRESH_EXPIRATION_DELTA

            if isinstance(refresh_limit, timedelta):
                refresh_limit = refresh_limit.days * 24 * 3600 + refresh_limit.seconds

            expiration_timestamp = orig_iat + int(refresh_limit)
            now_timestamp = int(timezone.now().timestamp())

            if now_timestamp > expiration_timestamp:
                msg = _("Refresh has expired.")
                raise serializers.ValidationError(msg)
        else:
            msg = _("orig_iat field is required.")
            raise serializers.ValidationError(msg)

        new_payload = JSONWebTokenAuthentication.jwt_create_payload(user)
        new_payload["orig_iat"] = orig_iat

        return {
            "token": JSONWebTokenAuthentication.jwt_encode_payload(new_payload),
            "user": user,
            "issued_at": new_payload.get("issued_at", datetime.utcnow().isoformat()),
        }


class BaseRefreshAuthTokenSerializer(RefreshJSONWebTokenSerializer):
    """RefreshAuthTokenSerializer"""

    def validate(self, data: dict) -> dict:
        """validate"""
        if api_settings.JWT_AUTH_COOKIE and data["token"] == "keep":
            data["token"] = JSONWebTokenAuthentication.get_token_from_request(
                self.context["request"]
            )
        return super().validate(data)
