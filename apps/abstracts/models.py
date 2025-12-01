# Python modules
from typing import Any

# Django modules
from django.utils import timezone
from django.db import models


class SoftDeleteManager(models.Manager):
    """
    Manager that handle soft-deleting
    """
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(deleted_at__isnull = True)

   
class AllObjectsManager(models.Manager):
    """
    Manager that shows all objects
    """
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset()   


class AbstractSoftDeletableModel(models.Model):
    """
    Abstract model that handle cases with soft deleting in other models via inheritance
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = AllObjectsManager()
    
    class Meta:
        abstract = True

    def delete(self, *args: tuple[Any, ...], **kwargs: dict[Any, Any]):
        """
        Soft deleting proccess
        """
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at", "updated_at"])