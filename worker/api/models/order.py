from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class OrderItem(models.Model, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("order item id"), primary_key=True)
    order = models.ForeignKey(to="api.OrderDetail", on_delete=models.CASCADE)
    product = models.ForeignKey(to="api.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(_("product quantity"))

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")


class OrderDetail(models.Model, CreateAndUpdateModelMixin):
    id = models.UUIDField(_("order id"), primary_key=True)
    user = models.ForeignKey(to="api.User", on_delete=models.CASCADE)
    total = models.FloatField(_("total amount"))
    status = models.CharField(_("order status"), max_length=255)

    class Meta:
        verbose_name = _("order detail")
        verbose_name_plural = _("order details")
