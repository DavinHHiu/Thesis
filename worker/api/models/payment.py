from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class PaymentMethod(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("payment method id"), primary_key=True)
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True, null=True)

    class Meta:
        verbose_name = _("payment method")
        verbose_name_plural = _("payment methods")


class Payment(models.Model, CreateAndUpdateModelMixin):
    id = models.BigIntegerField(_("payment id"), primary_key=True)
    order = models.ForeignKey(to="api.OrderDetail", on_delete=models.CASCADE)
    payment_method = models.ForeignKey(
        to="api.PaymentMethod", on_delete=models.SET_NULL, null=True
    )
    status = models.CharField(_("payment status"), max_length=255)
    total_amount = models.FloatField(_("total amount"))

    class Meta:
        verbose_name = _("payment")
        verbose_name_plural = _("payments")
