import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class ProductAttribute(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("product attribute id"), primary_key=True)
    type = models.CharField(_("product attribute type"), max_length=255)
    value = models.CharField(_("product attribute value"), max_length=255)

    class Meta:
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attributes")


class Product(models.Model, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("product id"), primary_key=True, default=uuid.uuid4)
    name = models.CharField(_("product name"), max_length=255)
    description = models.TextField(_("product description"))
    summary = models.TextField(_("product summary"))
    rating = models.IntegerField(_("product rating"), blank=True, null=True)
    categories = models.ManyToManyField(
        to="api.SubCategory",
        verbose_name=_("product categories"),
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")


class ProductSku(models.Model, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("product id"), primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey(
        to="api.Product", on_delete=models.CASCADE, related_name="product"
    )
    size = models.ForeignKey(
        to="api.ProductAttribute", on_delete=models.CASCADE, related_name="product_size"
    )
    color = models.ForeignKey(
        to="api.ProductAttribute",
        on_delete=models.CASCADE,
        related_name="product_color",
    )
    cover = models.ImageField(_("product cover"))
    sku = models.CharField(_("product sku"), max_length=255)
    price = models.FloatField(_("product price"))
    quantity = models.IntegerField(_("product quantity"))

    class Meta:
        verbose_name = _("product sku")
        verbose_name_plural = _("product skus")
