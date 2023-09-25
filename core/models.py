from django.db import models
from django.utils import timezone

__all__ = [
    'TimeStampedModel', 
    'SoftDeleteModel'
]

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False, editable=False)
    deleted_at = models.DateTimeField(null=True, blank=True, editable=False)
    
    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        return super().delete()

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()
        
    class DeletedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_deleted=True)
        
    class SoftDeleteModelManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(is_deleted=False)

        def delete(self):
            values = {"is_deleted": True, "deleted_at": timezone.now()}
            return self.update(**values)

        def restore(self):
            values = {"is_deleted": False, "deleted_at": None}
            return self.update(**values)

        def hard_delete(self):
            return super().delete()

    objects = SoftDeleteModelManager()
    deleted_objects = DeletedManager()
    all_objects = models.Manager()
