from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task
from api import serializers

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/'
    }
    return Response(api_urls)



@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def TaskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks , many = True)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def TaskCreate(request):
    serializer = TaskSerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


