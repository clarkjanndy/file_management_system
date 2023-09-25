from django.urls import path
from .yasg_schema import schema_view

from api import views


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('users/', views.UserListCreate.as_view()),
    path('users/<int:id>', views.UserById.as_view()),
    
    path('departments/', views.DepartmentListCreate.as_view()),
    path('departments/<int:id>', views.DepartmentById.as_view()),
    
    path('files/', views.FileListCreate.as_view()),
    path('files/backup', views.FileBackUp.as_view()),
    path('files/aggregate', views.FileAggregate.as_view())
]
