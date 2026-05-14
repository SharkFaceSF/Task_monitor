import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import Task
import time


@shared_task
def parse_url_task(task_id):
    task = Task.objects.get(id=task_id)
    task.status = 'processing'
    task.save()

    try:
        time.sleep(10) 
        
        response = requests.get(task.url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        result = {
            "links_count": len(soup.find_all('a')),
            "h1_count": len(soup.find_all('h1')),
            "title": soup.title.string if soup.title else "No title"
        }
        
        task.result = result
        task.status = 'completed'
    except Exception as e:
        task.result = {"error": str(e)}
        task.status = 'error'
    
    task.save()
