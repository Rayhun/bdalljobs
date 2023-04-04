# DJANGO IMPORTS
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CommonFieldModel(models.Model):
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_createdby"
    )
    is_active = models.BooleanField(
        _('Is Active'), default=True
    )
    order = models.IntegerField(
        _("Order"), blank=True, null=True
    )
    is_deleted = models.BooleanField(
        _('Is Deleted'), default=False
    )
    created_at = models.DateTimeField(
        _('Created At'), auto_now_add=True, null=True
    )
    update_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_updated"
    )
    last_updated = models.DateTimeField(
        _('Last Updated'), auto_now=True, null=True
    )
    deleted_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        blank=True, null=True, related_name="%(app_label)s_%(class)s_deleted"
    )
    deleted_at = models.DateTimeField(
        _('Deleted At'), blank=True, null=True
    )

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        abstract = True
