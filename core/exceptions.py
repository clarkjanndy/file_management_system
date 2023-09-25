from django.conf import settings

from rest_framework.exceptions import APIException, ValidationError, AuthenticationFailed, NotAuthenticated, MethodNotAllowed, PermissionDenied
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

from django.utils.translation import gettext_lazy as _

class ClientError(APIException):
    '''
    Custom exception for client-side related errors.
    '''
    
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Invalid request.')
    default_code = 'BAD_REQUEST'

    def __init__(self, detail=default_detail, status_code=status_code, code = default_code):
        self.detail = {
            'success': False,
            'code': code,
            'message': detail
        }
        self.status_code = status_code 

class SerializerValidationError(ValidationError):
    '''
    Custom exception for serializer field validation. Normally raised during field valdiation in serializers.    
    Note: Do not use in raising validation error. Always use serializers.ValidationError when overriding validate method.
    '''
   
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Invalid input.')
    default_code = 'BAD_REQUEST'

    def __init__(self, detail=default_detail, status_code=status_code, code = default_code):       
        self.detail = {
            'success': False,
            'code': code,
            'errors': detail,
        }       
        self.status_code = status_code
    

def custom_exception_handler(exc, context):
    '''
    Custom exception handler for certain exceptions    
    Note: This handler only checks for generic error,  404 and 403 are handled in views.
    '''
    # Call the default DRF exception handler to get the standard error response.
    response = exception_handler(exc, context)
    
    if response: # check if response is returned and then check for other exceptions that may arise    
        if isinstance(exc, NotAuthenticated):        
            error_data = {
                'success': False,
                'code': "AUTHENTICATION_FAILED",
                "message": _('Authentication credentials were not provided.'),
            }
            return Response(error_data, status = 401) 

        elif isinstance(exc, AuthenticationFailed):        
            error_data = {
                'success': False,
                'code': "AUTHENTICATION_FAILED",
                "message": _('Incorrect authentication credentials.'),
            }
            return Response(error_data, status = 401) 
        
        elif isinstance(exc, MethodNotAllowed):       
            request = context['request']
            method = request.method
             
            error_data = {
                'success': False,
                'code': "METHOD_NOT_ALLOWED",
                "message": _(f'Method {method} not allowed.'),
            }
            return Response(error_data, status = 405)   
        
        elif isinstance(exc, PermissionDenied):       
                        
            error_data = {
                'success': False,
                'code': "PERMISSION_DENIED",
                "message": _('You do not have permission to perform this action.'),
            }
            return Response(error_data, status = 403)      
        
        return response
    
    # check for any generic error if no response is returned 
    # comment out this part to see error stack trace during development (Django yellow screen)
    if isinstance(exc, Exception) and not settings.SHOW_ERROR_STACK_TRACE: 
        error_data = {
            'success': False,
            'code': "INTERNAL_SERVER_ERROR",
            "message": _('An internal server has error occurred.'),
            'detail': str(exc)
        }
        return Response(error_data, status = 500) 
    
    
