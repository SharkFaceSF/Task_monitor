import pytest
from django.urls import reverse
from .models import Task

@pytest.mark.django_db
def test_create_task_api(client):
    """Тест эндпоинта создания задачи"""
    url = reverse('task-list')  # это даст /api/tasks/
    data = {'url': 'https://google.com'}
    response = client.post(url, data)
    
    assert response.status_code == 201
    assert Task.objects.count() == 1
    assert Task.objects.get().url == 'https://google.com'
