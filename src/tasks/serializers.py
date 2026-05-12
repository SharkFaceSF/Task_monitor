from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'url', 'status', 'result', 'created_at', 'updated_at']
        read_only_fields = ['status', 'result', 'created_at', 'updated_at']
