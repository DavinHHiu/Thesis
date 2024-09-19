import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Cart(models.Model, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("cart id"), primary_key=True, default=uuid.uuid4())
    user = models.ForeignKey(to="api.User", on_delete=models.CASCADE)
    total = models.IntegerField(_("total amount"), default=0)

    class Meta:
        verbose_name = _("cart")
        verbose_name_plural = _("carts")


class CartItem(CreateAndUpdateModelMixin, models.Model):
    id = models.BigAutoField(_("cart item id"), primary_key=True)
    cart = models.ForeignKey(to="api.Cart", on_delete=models.CASCADE)
    product = models.ForeignKey(to="api.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(_("product quantity"))

    class Meta:
        verbose_name = _("cart item")
        verbose_name_plural = _("cart items")
