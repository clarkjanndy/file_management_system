from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

from api.models import Department


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **kwargs):
        try:
            User = get_user_model()
            
            username = input('Enter username: ')
            password = input('Enter password: ')
            birthday = input('Enter Birthday (YYYY-MM-DD): ')
            department = input('Enter department id: ')
       
            User.objects.create_superuser(
                department=Department.objects.get(id = department), 
                username=username, 
                password=password,
                birthday = birthday
            )
            
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        except Exception as err:
            self.stdout.write(self.style.ERROR(f'{str(err)}'))
            
        
