from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class ShipmentMethod(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("shipment method id"), primary_key=True)
    name = models.CharField(_("name"), max_length=255)
    fee = models.FloatField(_("shipping fee"))
    description = models.TextField(_("description"), blank=True, null=True)

    class Meta:
        verbose_name = _("shipment method")
        verbose_name_plural = _("shipment methods")


class Shipment(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("shipment id"), primary_key=True)
    order = models.ForeignKey(
        to="api.OrderDetail", on_delete=models.CASCADE, verbose_name=_("order")
    )
    shipping_method = models.ForeignKey(
        to="api.ShipmentMethod", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(_("shipping status"), max_length=255)

    class Meta:
        verbose_name = _("shipment")
        verbose_name_plural = _("shipments")
