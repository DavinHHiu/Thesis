from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Shipment(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("shipment id"), primary_key=True)
    order = models.ForeignKey(
        to="api.OrderDetail", on_delete=models.CASCADE, verbose_name=_("order")
    )
    shipping_method = models.CharField(_("shipping method"), max_length=255)
    shipping_fee = models.FloatField(_("shipping fee"))
    status = models.CharField(_("shipping status"), max_length=255)

    class Meta:
        verbose_name = _("shipment")
        verbose_name_plural = _("shipments")
