from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class PaymentMethod(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("payment method id"), primary_key=True)
    icon = models.ImageField(_("payment method icon"), blank=True, null=True)
    name = models.CharField(_("payment method name"), max_length=255)
    value = models.CharField(_("payment method value"), max_length=255)
    description = models.TextField(
        _("payment method description"), blank=True, null=True
    )
    is_active = models.BooleanField(_("active status"), default=True)

    class Meta:
        verbose_name = _("payment method")
        verbose_name_plural = _("payment methods")


class Payment(models.Model, CreateAndUpdateModelMixin):
    id = models.BigAutoField(_("payment id"), primary_key=True)
    order = models.OneToOneField(
        to="api.OrderDetail",
        on_delete=models.CASCADE,
        verbose_name="order",
        related_name="payment",
    )
    payment_method = models.ForeignKey(
        to="api.PaymentMethod",
        on_delete=models.CASCADE,
        verbose_name=_("payment_method"),
    )
    total_amount = models.FloatField(_("total amount"))

    class Meta:
        verbose_name = _("payment")
        verbose_name_plural = _("payments")
