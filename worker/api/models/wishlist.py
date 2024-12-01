from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class WishList(CreateAndUpdateModelMixin, models.Model):
    id = models.BigAutoField(_("wishList id"), primary_key=True)
    product = models.ForeignKey(
        to="api.Product", on_delete=models.CASCADE, verbose_name=_("product")
    )
    user = models.ForeignKey(
        to="api.User",
        on_delete=models.CASCADE,
        verbose_name="user",
    )

    class Meta:
        verbose_name = _("wishlist")
        verbose_name_plural = _("wishlists")
