from rest_framework import serializers

from core.serializers import CustomModelSerializer, CustomSerializer

from api.models import File

__all__ = ['FileSerializer', 'FileAggregateSerializer']

class FileSerializer(CustomModelSerializer):
    
    class Meta:
        model = File
        fields = ('file', 'is_backed_up', 'last_back_up')
        read_only_fields = ('is_backed_up', 'last_back_up')
        
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        
        validated_data.update({"user": user})
                
        return super().create(validated_data)

class FileAggregateSerializer(CustomSerializer):
    department_name = serializers.CharField()
    file_comsumption = serializers.DecimalField(max_digits=10, decimal_places=2)


