import os
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
from api.models import Address, District, Province, User, Ward
from api.v1.serializers import EmailValidationSerializer


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False, read_only=True)
    avatar = serializers.ImageField(required=False)
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False, allow_null=True)
    last_name = serializers.CharField(required=False, allow_null=True)
    email = serializers.EmailField()
    password = serializers.CharField(required=False, write_only=True)
    birth_of_date = serializers.DateField(required=False, allow_null=True)
    tel = serializers.CharField(max_length=10, required=False, allow_null=True)

    class Meta:
        model = User
        fields = [
            "id",
            "avatar",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "birth_of_date",
            "tel",
        ]

    @transaction.atomic
    def validate(self, data):
        return super().validate(data)

    @transaction.atomic
    def create(self, validated_data):
        serializer = EmailValidationSerializer(data=validated_data)
        serializer.is_valid(raise_exception=True)

        existing_users = User.objects.filter(email=validated_data["email"])
        if len(existing_users) > 0:
            msg = _("Email already exists")
            raise serializers.ValidationError(msg)
        try:
            ModelClass = self.Meta.model
            instance = ModelClass._default_manager.create_user(**validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError({"detail": str(e)})

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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request", None)
        if request and instance.avatar:
            representation["avatar"] = request.build_absolute_uri(instance.avatar.url)
        return representation


class PasswordResetSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    retype_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = self.context["request"].user
        if not user.check_password(attrs["old_password"]):
            msg = _("Invalid old password")
            raise serializers.ValidationError({"error": msg})
        if attrs["new_password"] != attrs["retype_password"]:
            msg = _("Passwords do not match")
            raise serializers.ValidationError({"error": msg})
        return attrs

    def create(self, data):
        user = self.context["request"].user
        user.set_password(data["new_password"])
        user.save()
        return user


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    retype_password = serializers.CharField()

    def validate(self, data):
        existing_email = User.objects.filter(email=data["email"])
        if existing_email.exists():
            msg = _("Email already exists")
            raise serializers.ValidationError(msg)
        if data["password"] != data["retype_password"]:
            msg = _("Passwords do not match")
            raise serializers.ValidationError(msg)

        data.pop("retype_password", None)

        return data

    def create(self, validated_data):
        ModelClass = User
        instance = ModelClass._default_manager.create_user(**validated_data)
        return instance


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    user_id = serializers.CharField(source="user.id", read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    city = serializers.CharField()
    district = serializers.CharField()
    ward = serializers.CharField()
    address_1 = serializers.CharField()
    address_2 = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    display_address1 = serializers.CharField(
        required=False, allow_blank=True, allow_null=True
    )
    tel = serializers.CharField(max_length=10)
    representative = serializers.CharField()

    class Meta:
        model = Address
        fields = [
            "id",
            "user_id",
            "title",
            "city",
            "district",
            "ward",
            "address_1",
            "address_2",
            "tel",
            "representative",
            "display_address1",
        ]

    @transaction.atomic
    def create(self, validated_data):
        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(
            user=self.context["request"].user, **validated_data
        )
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        try:
            province = Province.objects.get(code=validated_data.pop("city", None)).name
            district = District.objects.get(
                code=validated_data.pop("district", None)
            ).name
            ward = Ward.objects.get(code=validated_data.pop("ward", None)).name
            validated_data["display_address1"] = f"{ward}, {district}, {province}"

        except (Province.DoesNotExist, District.DoesNotExist, Ward.DoesNotExist) as e:
            msg = {
                Province.DoesNotExist: _("Province does not exist"),
                District.DoesNotExist: _("District does not exist"),
                Ward.DoesNotExist: _("Ward does not exist"),
            }
            raise serializers.ValidationError(msg[type(e)])
        for attr, value in validated_data.items():
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

        serializer = EmailValidationSerializer(
            data={"email": data.get(self.username_field)}
        )
        serializer.is_valid(raise_exception=True)

        user = authenticate(self.context["request"], **credentials)

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
