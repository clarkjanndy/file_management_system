from django.db import models

from core.models import SoftDeleteModel, TimeStampedModel

__all__ = ['Department']

class Department(TimeStampedModel, SoftDeleteModel):
    name = models.CharField(max_length=150)
    description = models.TextField()
   
    class Meta:
        app_label = 'api'
        db_table = 'departments'
        
    def __str__(self):
        return f"{self.name}"
        
    