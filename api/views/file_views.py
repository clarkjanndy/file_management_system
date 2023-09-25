from django.db.models import Sum, F

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from api.tasks import back_up_files
from api.serializers import FileSerializer, FileAggregateSerializer
from api.models import File, Department

__all__ = ['FileListCreate', 'FileBackUp', 'FileAggregate']

class FileListCreate(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = FileSerializer
    queryset = File.objects.all()
    
    def get_queryset(self):
        request = self.request
        return super().get_queryset().filter(user = request.user)
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data
        
        return Response({"success": True, "code": "SUCCESS", "data": data})
    
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        rows = response.data
        count = len(rows)
        
        return Response({"success": True, "code": "SUCCESS", "data": {"count": count, "rows": rows}})

class FileBackUp(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = File.objects.all()

    def get_queryset(self):
        request = self.request
        return super().get_queryset().filter(user = request.user)

    def post(self, request, *args, **kwargs):

        files = self.get_queryset()
        if files:
            back_up_files(files)

        return Response({"success": True, "code": "SUCCESS", "message": "Task of backing up files has started."}) 

class FileAggregate(GenericAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = File.objects.all()
    serializer_class = FileAggregateSerializer

    def get(self, request, *args, **kwargs):
        query = File.objects.select_related('user__department').values('user__department__id').annotate(file_comsumption = Sum('file_size'), department_name = F('user__department__name'))

        serializer = self.serializer_class(query, many = True)  
        data = serializer.data

        return Response({"success": True, "code": "SUCCESS", "data": data})


        


