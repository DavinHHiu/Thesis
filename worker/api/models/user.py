import os
import random
import uuid

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image

from api.models.mixins import CreateAndUpdateModelMixin

from . import Cart


class Address(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("address id"), primary_key=True)
    user = models.ForeignKey(
        to="api.User",
        on_delete=models.CASCADE,
        null=True,
        verbose_name=_("user"),
    )
    title = models.CharField(_("address title"), max_length=255, null=True, blank=True)
    city = models.CharField(_("city"), max_length=255)
    district = models.CharField(_("district"), max_length=255)
    ward = models.CharField(_("ward"), max_length=255)
    address_1 = models.CharField(_("address 1"), max_length=255, blank=True)
    address_2 = models.CharField(_("address 2"), max_length=255, null=True, blank=True)
    tel = models.CharField(
        _("telephone number"),
        max_length=15,
        blank=True,
    )
    representative = models.CharField(_("representative"), max_length=255, blank=True)
    display_address1 = models.CharField(_("display address"), max_length=255)
    is_default = models.BooleanField(_("is default address"), default=False)

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email or not password:
            raise ValueError("Email and password is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)

        if "avatar" in extra_fields:
            avatar = extra_fields.pop("avatar")

        media_root = settings.MEDIA_ROOT
        avatar_directory = media_root / "images" / "avatars" / "custom"

        if not os.path.exists(avatar_directory):
            os.makedirs(avatar_directory, exist_ok=True)

        avatar_path = avatar_directory / f"{str(user.id)}.jpg"
        if "avatar" in extra_fields:
            pil_image = Image.open(avatar)
        else:
            default_img_dir = os.path.join(media_root, "images", "avatars", "default")

            img_paths = os.listdir(default_img_dir)
            random_img_idx = random.randint(0, len(img_paths) - 1)
            img_path = os.path.join(default_img_dir, img_paths[random_img_idx])

            pil_image = Image.open(img_path)

        pil_image = pil_image.convert("RGB")
        pil_image.save(avatar_path, format="JPEG")

        user.avatar = os.path.relpath(avatar_path, media_root)

        if not user.username:
            user.username = self.get_username(email)

        user.save(using=self._db)

        Cart.objects.create(user=user)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def with_perm(
        self, perm, is_active=True, include_superusers=True, backend=None, obj=None
    ):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    "You have multiple authentication backends configured and "
                    "therefore must provide the `backend` argument."
                )
        elif not isinstance(backend, str):
            raise TypeError(
                "backend must be a dotted import path string (got %r)." % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, "with_perm"):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

    def get_username(self, email):
        return email.split("@")[0]


class User(AbstractUser, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("user id"), primary_key=True, default=uuid.uuid4)
    avatar = models.ImageField(_("user avatar"), blank=True, null=True)
    first_name = models.CharField(
        _("first name"),
        max_length=255,
        blank=True,
        null=True,
    )
    last_name = models.CharField(_("last name"), max_length=255, blank=True, null=True)
    email = models.EmailField(
        _("email adress"),
        max_length=255,
        unique=True,
    )
    username = models.CharField(_("username"), max_length=255, blank=True, null=True)
    password = models.CharField(
        _("password"),
        max_length=255,
        blank=True,
    )
    birth_of_date = models.DateField(
        _("birth of date"),
        blank=True,
        null=True,
    )
    tel = models.CharField(_("telephone number"), max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
