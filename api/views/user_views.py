from django.core.exceptions import ObjectDoesNotExist

from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from core.exceptions import ClientError

from api.serializers import UserSerializer
from api.models import User

__all__ = ['UserListCreate', 'UserById']

class UserListCreate(ListCreateAPIView):
    # only admin can view all and create new users, users can still register 
    permission_classes = (IsAdminUser, ) 
    serializer_class = UserSerializer   
    queryset = User.objects.all()
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data
        
        return Response({"success": True, "code": "SUCCESS", "data": data})
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        rows = response.data
        count = len(rows)
        
        return Response({"success": True, "code": "SUCCESS", "data": {"count": count, "rows": rows}})

class UserById(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser, ) 
    serializer_class = UserSerializer   
    queryset = User.objects.all()   
    lookup_field = 'id'     
    
    def get_object(self):
        try:
            obj = self.queryset.all().get(id = self.kwargs['id'])
            return obj    
       
        except ObjectDoesNotExist as e:
            raise ClientError(detail = str(e), status_code = 404, code = 'NOT_FOUND')
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data
        
        return Response({"success": True, "code": "SUCCESS", "data": data})

    def patch(self, request, *args, **kwargs):
        response = super().patch(request, *args, **kwargs)
        data = response.data
        
        return Response({"success": True, "code": "SUCCESS", "data": data})
    
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        data = response.data
        
        return Response({"success": True, "code": "SUCCESS", "data": data})
        


