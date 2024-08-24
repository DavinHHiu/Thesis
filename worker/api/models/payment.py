from django.db import models
from django.utils.translation import gettext_lazy as _

from api.models.mixins import CreateAndUpdateModelMixin


class Payment(models.Model, CreateAndUpdateModelMixin):
    id = models.BigIntegerField(_("payment id"), primary_key=True)
    order = models.ForeignKey(to="api.OrderDetail", on_delete=models.CASCADE)
    payment_method = models.CharField(_("payment method"), max_length=255)
    status = models.CharField(_("payment status"), max_length=255)
    total_amount = models.FloatField(_("total amount"))

    class Meta:
        verbose_name = _("payment")
        verbose_name_plural = _("payments")
