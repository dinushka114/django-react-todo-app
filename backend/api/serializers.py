from django.db import models
from django.db.models.base import Model
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Task
        fiels = '__all__'