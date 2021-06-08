from django.db import models
from django.http import response
from rest_framework import generics, serializers
from .serializers import ProjectsSerializer, TasksSerializer
import requests
from rest_framework import generics
from .models import Tasks

from rest_framework.views import APIView




from project.models import Projects, Tasks


class ProjectList(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    
class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class TaskList(generics.ListCreateAPIView):

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer


