from django.contrib import admin
from django.contrib import messages
from django.utils import timezone

class IsDeletedAliasFilter(admin.SimpleListFilter):
    title = 'Deleted'  # Title for the filter displayed in the admin

    parameter_name = 'is_deleted'  # The parameter name used in the URL query string

    def lookups(self, request, model_admin):
        # Define the filter options with custom labels
        return (
            (0, "Active"),  
            (1, "Deleted"),  
        )

    def queryset(self, request, queryset):
        # Apply the selected filter option to the queryset
        if self.value() == 1:
            return queryset.filter(is_deleted = True)
        
        elif self.value() == 0:
            return queryset.filter(is_deleted = False)

class SofDeleteAdmin(admin.ModelAdmin):
    list_filter = (IsDeletedAliasFilter,)
        
    def delete_selected(modeladmin, request, queryset):
        count = queryset.count()
        model = modeladmin.model.__name__
        
        queryset.update(is_deleted = True, deleted_at = timezone.now())
        messages.success(request, f"{count} {model} object(s) deleted succesfully.")
        
    def restore_selected(modeladmin, request, queryset):
        count = queryset.count()
        model = modeladmin.model.__name__
        
        queryset.update(is_deleted = False, deleted_at = None)
        messages.success(request, f"{count} {model} object(s) restored succesfully.")
          
    actions = (delete_selected, restore_selected, )
        
    def get_queryset(self, request):
        # Override the queryset to include soft-deleted objects when requested
        if request.GET.get('is_deleted') == '1':
            return self.model.deleted_objects.all()
        
        elif request.GET.get('is_deleted') == '0':
            return self.model.objects.all()
        
        return self.model.all_objects.all()