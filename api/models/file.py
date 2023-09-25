import os
from django.db import models
from core.models import SoftDeleteModel, TimeStampedModel

__all__ = ['File']

def upload_file(instance, filename):
    user = instance.user
    department = user.department.name
    
    # upload the file to department/username/fielname.txt
    upload_dir = f"{department}/{user.username}/"
    
    # check if instance is already an existing record 
    if instance.pk:
        try:
            instance.refresh_from_db() # refresh from db to get the latest instance
            old_file = instance.file   # get the file field
            if old_file:  
                os.remove(old_file.path) # remove the file in directory
        
        except Exception as err:
            print(str(err))
            
    # return the upload path           
    return os.path.join(upload_dir, filename)

class File(TimeStampedModel, SoftDeleteModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    file = models.FileField(upload_to = upload_file)
    file_size = models.FloatField(editable = False)
    is_backed_up = models.BooleanField(default = False)
    last_back_up = models.DateTimeField(null = True, blank = True)

   
    class Meta:
        app_label = 'api'
        db_table = 'files'
        
    def __str__(self):
        return f"{self.file}"

    def save(self, *args, **kwargs):
        if self.file:
            file_size_mb = round(self.file.size / (1024 * 1024), 2)
            self.file_size = file_size_mb
            
        super().save(*args, **kwargs)

   

        

        
        
    