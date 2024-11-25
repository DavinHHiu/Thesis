from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Province(models.Model, CreateAndUpdateModelMixin):
    code = models.IntegerField(_("province code"), primary_key=True)
    name = models.CharField(_("province name"), max_length=255)
    division_type = models.CharField(_("province type"), max_length=255)
    codename = models.CharField(_("province codename"), max_length=255)
    phone_code = models.IntegerField(_("province phone code"))
    is_active = models.BooleanField(_("active status"), default=True)

    class Meta:
        verbose_name = _("province")
        verbose_name_plural = _("provinces")


class District(models.Model, CreateAndUpdateModelMixin):
    code = models.IntegerField(_("district code"), primary_key=True)
    name = models.CharField(_("district name"), max_length=255)
    division_type = models.CharField(_("district type"), max_length=255)
    codename = models.CharField(_("district codename"), max_length=255)
    province = models.ForeignKey(
        to="api.Province",
        verbose_name=_("province"),
        on_delete=models.CASCADE,
        related_name="districts",
    )
    is_active = models.BooleanField(_("active status"), default=True)

    class Meta:
        verbose_name = _("district")
        verbose_name_plural = _("districts")


class Ward(models.Model, CreateAndUpdateModelMixin):
    code = models.IntegerField(_("ward code"), primary_key=True)
    name = models.CharField(_("ward name"), max_length=255)
    division_type = models.CharField(_("ward type"), max_length=255)
    codename = models.CharField(_("ward codename"), max_length=255)
    district = models.ForeignKey(
        to="api.District",
        verbose_name="district",
        on_delete=models.CASCADE,
        related_name="wards",
    )
    is_active = models.BooleanField(_("active status"), default=True)

    class Meta:
        verbose_name = _("ward")
        verbose_name_plural = _("wards")
