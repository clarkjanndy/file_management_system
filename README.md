# File Management System
## Follow these steps to clone this repository

! git clone https://github.com/clarkjanndy/file_management_system <br>
! pip install -r requirements.txt

### Run migrations
! python manage.pt makemigrations <br>
! python manage.py migrate

### Populate DB using custom management commands
! python manage.py createdepartment - <b>creates a department</b><br>
! python manage.py api_createsuperuser - <b>creates a starting superuser for you to start using the apis</b><br>


