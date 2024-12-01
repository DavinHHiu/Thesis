from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class ShipmentMethod(CreateAndUpdateModelMixin, models.Model):
    id = models.BigAutoField(_("shipment method id"), primary_key=True)
    name = models.CharField(_("shipment method name"), max_length=255)
    value = models.CharField(_("shipment method value"), max_length=255)
    description = models.TextField(
        _("shipment method description"), blank=True, null=True
    )
    estimated_shipping_days = models.IntegerField(_("estimated shipping days"))
    shipping_fee = models.FloatField(_("shipping fee"))
    is_active = models.BooleanField(_("active status"), default=True)

    class Meta:
        verbose_name = _("shipment method")
        verbose_name_plural = _("shipment methods")


class Shipment(CreateAndUpdateModelMixin, models.Model):
    id = models.BigAutoField(_("shipment id"), primary_key=True)
    order = models.OneToOneField(
        to="api.OrderDetail",
        on_delete=models.CASCADE,
        verbose_name=_("order"),
        related_name="shipment",
    )
    receive_address = models.ForeignKey(to="api.Address", on_delete=models.CASCADE)
    shipment_method = models.ForeignKey(
        to="api.ShipmentMethod",
        on_delete=models.CASCADE,
        verbose_name=_("shipment_method"),
    )
    shipping_date = models.DateTimeField()

    class Meta:
        verbose_name = _("shipment")
        verbose_name_plural = _("shipments")

    def save(self, *args, **kwargs):
        if (
            self.shipment_method
            and self.shipment_method.estimated_shipping_days is not None
        ):
            self.shipping_date = timezone.now() + timedelta(
                days=self.shipment_method.estimated_shipping_days
            )
        super().save(*args, **kwargs)
