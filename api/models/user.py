from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from core.models import SoftDeleteModel

__all__ = ['User']

 # creates a manager that inherits both Usermanager and SoftDeleteModelManager
class MyUserManager(UserManager, SoftDeleteModel.SoftDeleteModelManager):
    pass

class User(SoftDeleteModel, AbstractUser):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    position = models.CharField(max_length = 150)
    middle_name = models.CharField(max_length=150, null = True, blank = True)
    suffix = models.CharField(max_length=30, null = True, blank = True)
    birthday = models.DateField()
    
    class Meta:
        app_label = 'api'
        db_table = 'users'
        
    objects = MyUserManager()
    
   
    
        
    