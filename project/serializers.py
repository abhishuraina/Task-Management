from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Projects, Tasks


class TasksSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Tasks
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):

    # tasks =  serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    tasks = TasksSerializer(many=True, read_only = True)
    
    class Meta:
        model = Projects
        fields = ('id', 'name', 'description', 'duration', 'completed' , 'tasks')
