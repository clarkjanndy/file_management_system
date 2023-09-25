from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from core.admin import SofDeleteAdmin
from api.models import User, Department, File

# Create admin managers here.
class UserAdmin(SofDeleteAdmin, DefaultUserAdmin):
    fieldsets = (
        (_("Credentials"), {"fields": ("username", "password")}),
        (_("Information"), {"fields": ("department", "email", "first_name", "middle_name", "last_name", "suffix", "birthday")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ('username', 'email', 'last_login', 'is_superuser', 'date_joined')
     
class DepartmentAdmin(SofDeleteAdmin):
    list_display = ('name', 'description', 'created_at', 'modified_at')
    search_fields = ("name", )
    
class FileAdmin(SofDeleteAdmin):
    list_display = ('user', 'file', 'file_size', 'is_backed_up', 'last_back_up','created_at')
    search_fields = ("file", )

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(File, FileAdmin)