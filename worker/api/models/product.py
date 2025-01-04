import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class ProductAttribute(CreateAndUpdateModelMixin, models.Model):
    id = models.BigAutoField(_("product attribute id"), primary_key=True)
    type = models.CharField(_("product attribute type"), max_length=255)
    value = models.CharField(_("product attribute value"), max_length=255)

    class Meta:
        verbose_name = _("product attribute")
        verbose_name_plural = _("product attributes")


class Product(CreateAndUpdateModelMixin, models.Model):
    id = models.UUIDField(_("product id"), primary_key=True, default=uuid.uuid4)
    name = models.CharField(_("product name"), max_length=255)
    description = models.TextField(_("product description"))
    summary = models.TextField(_("product summary"), null=True, blank=True)
    rating = models.DecimalField(
        _("product rating"), max_digits=3, decimal_places=2, blank=True, default=0
    )
    categories = models.ManyToManyField(
        to="api.SubCategory",
        verbose_name=_("product categories"),
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")


class ProductSku(CreateAndUpdateModelMixin, models.Model):
    id = models.UUIDField(_("product id"), primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey(
        to="api.Product", on_delete=models.CASCADE, related_name="skus"
    )
    size = models.ForeignKey(
        to="api.ProductAttribute", on_delete=models.CASCADE, related_name="product_size"
    )
    color = models.ForeignKey(
        to="api.ProductAttribute",
        on_delete=models.CASCADE,
        related_name="product_color",
    )
    sku = models.CharField(_("product sku"), max_length=255)
    price = models.FloatField(_("product price"))
    quantity = models.IntegerField(_("product quantity"))

    class Meta:
        verbose_name = _("product sku")
        verbose_name_plural = _("product skus")


class ProductImage(CreateAndUpdateModelMixin, models.Model):
    id = models.BigAutoField(_("product image id"), primary_key=True)
    image = models.ImageField(_("product image"), null=True, blank=True)
    feature = models.TextField(_("product feature"), null=True, blank=True)
    product_sku = models.ForeignKey(
        to="api.ProductSku", on_delete=models.CASCADE, related_name="images"
    )

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")
