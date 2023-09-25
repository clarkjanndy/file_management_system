from rest_framework import serializers

from core.serializers import CustomModelSerializer

from api.models import User
from .department_serializers import DepartmentSerializer

__all__ = ['UserSerializer']

class UserSerializer(CustomModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id','department', 'username', 'password', 'first_name', 'middle_name', 'last_name', 'suffix', 'email', 
                  'birthday', 'position', 'is_deleted')
        
    def create(self, validated_data):
        # we use create user here instead of create so that we can retain automatic values of the user model
        user = User.objects.create_user(**validated_data)
        
        return user
    
    def update(self, instance, validated_data):
        
        # we won't allow edit of password here change password must be done by account owner
        if 'password' in validated_data:
            validated_data.pop('password')
        
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.update({"department": instance.department.name})
        
        return representation

        
        

