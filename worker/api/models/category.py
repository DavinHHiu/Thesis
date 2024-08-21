from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Category(models.Model, CreateAndUpdateModelMixin):
    id = models.BigIntegerField(_("category id"), primary_key=True)
    name = models.CharField(_("category name"), max_length=255)
    description = models.TextField(_("category description"), blank=True, null=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")


class SubCategory(models.Model, CreateAndUpdateModelMixin):
    id = models.BigIntegerField(_("subcategory id"), primary_key=True)
    category = models.ForeignKey(
        to="Category",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=_("parent category"),
    )
    name = models.CharField(_("subcategory name"), max_length=255)
    description = models.TextField(_("subcategory description"), blank=True, null=True)

    class Meta:
        verbose_name = _("subcategory")
        verbose_name_plural = _("subcategories")
