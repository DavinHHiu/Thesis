from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Settings(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(to="api.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("setting")
        verbose_name_plural = _("settings")


class SettingItems(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("setting item id"), primary_key=True)
    setting = models.ForeignKey(
        to="api.Settings",
        verbose_name=_("setting"),
        on_delete=models.CASCADE,
        related_name="items",
    )
    key = models.CharField(_("key"), max_length=255)
    value = models.CharField(_("value"), max_length=255)
    description = models.TextField(_("description"))
    is_active = models.BooleanField(_("active"), default=True)

    class Meta:
        verbose_name = _("setting item")
        verbose_name_plural = _("setting items")
        unique_together = ("setting", "key")
