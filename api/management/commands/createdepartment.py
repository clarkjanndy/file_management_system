from django.core.management import BaseCommand

from api.models import Department

class Command(BaseCommand):
    help = 'Create a department'

    def handle(self, *args, **kwargs):
        try:
            name = input('Enter department name: ')
            description = input('Enter department description: ')
            
            Department.objects.create(
                name = name,
                description = description
            )
    
            self.stdout.write(self.style.SUCCESS('Department created successfully.'))
            
        except Exception as err:
             self.stdout.write(self.style.ERROR(f'{str(err)}'))
            
