# Python modules
from typing import Any

# Django modules
from django.utils import timezone
from django.db import models


class AbstractSoftDeletableModel(models.Model):
    """
    Abstract model that handle cases with soft deleting in other models via inheritance
    """

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract = True

    def delete(self, *args: tuple[Any, ...], **kwargs: dict[Any, Any]):
        """
        Soft deleting proccess
        """
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])