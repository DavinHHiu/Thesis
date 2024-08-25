import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Address(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("address id"), primary_key=True)
    user = models.ForeignKey(
        to="api.User",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("user"),
    )
    title = models.CharField(_("address title"), max_length=255)
    address_1 = models.CharField(_("address 1"), max_length=255, blank=True)
    address_2 = models.CharField(_("address 2"), max_length=255, blank=True)
    zipcode = models.CharField(_("zipcode"), max_length=255, blank=True)
    tel = models.CharField(
        _("telephone number"),
        max_length=15,
        blank=True,
    )

    class Meta:
        verbose_name = _("address")
        verbose_name_plural = _("addresses")


class User(AbstractUser, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("user id"), primary_key=True, default=uuid.uuid4())
    avatar = models.ImageField(_("user avatar"))
    first_name = models.CharField(
        _("first name"),
        max_length=255,
        blank=True,
    )
    last_name = models.CharField(_("last name"), max_length=255, blank=True)
    email = models.EmailField(
        _("email adress"),
        max_length=255,
        unique=True,
    )
    password = models.CharField(_("password"), max_length=255)
    birth_of_date = models.DateField(_("birth of date"))
    tel = models.CharField(_("telephone number"), max_length=15)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
