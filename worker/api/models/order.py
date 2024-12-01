import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.consts import base_consts
from api.models.mixins import CreateAndUpdateModelMixin


class OrderDetail(CreateAndUpdateModelMixin, models.Model):
    id = models.CharField(_("order id"), primary_key=True, max_length=255)
    user = models.ForeignKey(to="api.User", on_delete=models.CASCADE)
    status = models.CharField(
        _("order status"),
        max_length=255,
        choices=base_consts.ORDER_STATUSES,
        default=base_consts.ORDER_STATUS_PENDING,
    )
    total_quantity = models.IntegerField(_("total quantity"))

    class Meta:
        verbose_name = _("order detail")
        verbose_name_plural = _("order details")


class OrderItem(CreateAndUpdateModelMixin, models.Model):
    id = models.UUIDField(_("order item id"), primary_key=True, default=uuid.uuid4)
    order = models.ForeignKey(to="api.OrderDetail", on_delete=models.CASCADE)
    product_sku = models.ForeignKey(to="api.ProductSku", on_delete=models.CASCADE)
    quantity = models.IntegerField(_("product quantity"))
    subtotal = models.FloatField(_("subtotal"), default=0)

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")

    def save(self, *args, **kwargs):
        self.subtotal = self.product_sku.price * self.quantity
        super().save(*args, **kwargs)
