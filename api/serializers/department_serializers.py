from core.serializers import CustomModelSerializer

from api.models import Department

__all__ = ['DepartmentSerializer']

class DepartmentSerializer(CustomModelSerializer):
    
    class Meta:
        model = Department
        fields = ('id','name', 'description', 'created_at', 'modified_at')
        

