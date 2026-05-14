from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .tasks import parse_url_task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        parse_url_task.delay(instance.id)
