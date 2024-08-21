from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class ProductAttribute(models.Model, CreateAndUpdateModelMixin):
    id = models.BigIntegerField(_("product attribute id"), primary_key=True)
    type = models.CharField(_("product attribute type"), max_length=255)
    value = models.CharField(_("product attribute value"), max_length=255)

    class Meta:
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attributes")


class ProductBase(models.Model, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("product id"), primary_key=True)
    name = models.CharField(_("product name"), max_length=255)
    description = models.TextField(_("product description"))
    summary = models.TextField(_("product summary"))
    cover = models.ImageField(_("product cover"))
    categories = models.ManyToManyField(
        to="api.SubCategory",
        blank=True,
        verbose_name=_("product categories"),
    )


class Product(ProductBase):
    size = models.ForeignKey(to="ProductAttribute", on_delete=models.CASCADE)
    color = models.ForeignKey(to="ProductAttribute", on_delete=models.CASCADE)
    sku = models.CharField(_("product sku"), max_length=255)
    price = models.FloatField(_("product price"))
    quantity = models.IntegerField(_("product quantity"))

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
