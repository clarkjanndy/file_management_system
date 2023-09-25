from django.utils import timezone
from api.models import File
# this should be a celery task but for the sake of example i choose to simplify it
def back_up_files(files):
    
    for file in files:
        try:
            file.is_backed_up = True
            file.last_back_up = timezone.now()
            file.save()

            print(f'sending success for {file}')
            
        except Exception as err:
            print("ERROR: ", err)
            print(f'sending failed for file {file}')
    
    return  
