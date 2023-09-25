from rest_framework import serializers
from core.exceptions import SerializerValidationError

__all__ = [
    'CustomSerializer',
    'CustomModelSerializer',
    'SucessSerializer', 
    'Error400Serializer', 
    'Error401Serializer',
    'Error403Serializer', 
    'Error404Serializer',
    'Error405Serializer',
    'Error500Serializer', 
]
  
class CustomSerializer(serializers.Serializer):
    '''
    Custom Serializer class that will return only the first error of a field during validation.
    '''
    
    def is_valid(self, *, raise_exception = False):
        if not super().is_valid(): # call the method from the parent class
            errors = {}
            for field, field_errors in self.errors.items():
                errors[field] = field_errors[0]  # only include the first error message for each field

            raise SerializerValidationError(errors, 400)

class CustomModelSerializer(serializers.ModelSerializer, CustomSerializer):
    '''
    Custom ModelSerializer class that will return only the first error of a field during validation.
    '''
    
    class Meta:
        pass

# these serializers will be used for documentation purposes (Swagger)       
class SucessSerializer(serializers.Serializer):
   success = serializers.BooleanField(default = True)
   code = serializers.CharField(default = 'SUCCESS')
   message = serializers.CharField(required = False)
   data = serializers.JSONField(required = False)
                     
class Error400Serializer(serializers.Serializer):
   success = serializers.BooleanField(default = False)
   code = serializers.CharField(default = 'BAD_REQUEST')
   message =  serializers.CharField(required = False)   
   errors = serializers.JSONField(required = False)
   
class Error401Serializer(serializers.Serializer):
   success = serializers.BooleanField(default = False)
   code = serializers.CharField(default = 'AUTHENTICATION_FAILED')
   message =  serializers.CharField(default = 'Incorrect authentication credentials.')
   
class Error403Serializer(serializers.Serializer):
   success = serializers.BooleanField(default = False)
   code = serializers.CharField(default = 'PERMISSION_DENIED')
   message = serializers.CharField(default = 'You do not have permission to perform this action.')
   
class Error404Serializer(serializers.Serializer):
   success = serializers.BooleanField(default = False)
   code = serializers.CharField(default = 'NOT_FOUND')
   message = serializers.CharField(default = 'Sorry, we cannot find the resource that you are trying to access.')
   
class Error405Serializer(serializers.Serializer):
   success = serializers.BooleanField(default = False)
   code = serializers.CharField(default = 'METHOD_NOT_ALLOWED')
   message = serializers.CharField(default = 'Method {method} not allowed.')
   
class Error500Serializer(serializers.Serializer):
    success = serializers.BooleanField(default = False)
    code = serializers.CharField(default = "INTERNAL_SERVER_ERROR")
    message = serializers.CharField(default = "An internal has server error occurred.")
    detail = serializers.CharField()
