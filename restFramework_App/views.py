from django.shortcuts import render
from rest_framework import viewsets
from . serializers import taskSerializers
from .models import Task
# Create your views here.

class taskViewset( viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class= taskSerializers
    
class notCompleted(viewsets.ModelViewSet):
    queryset=Task.objects.all().filter(task_completed=False)
    serializer_class= taskSerializers
    
class Completed(viewsets.ModelViewSet):
    queryset=Task.objects.all().filter(task_completed=True)
    serializer_class= taskSerializers
    
    