from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CreateAndUpdateModelMixin:
    create_at = models.DateTimeField(
        _("create_at"), auto_now_add=True, default=timezone.now()
    )
    update_at = models.DateTimeField(
        _("update_at"), auto_now=True, default=timezone.now()
    )

    class Meta:
        abstract = True
