from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('processing', 'В процессе'),
        ('completed', 'Завершено'),
        ('error', 'Ошибка'),
    ]

    url = models.URLField(verbose_name='URL для парсинга')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    result = models.JSONField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Task {self.id} - {self.url}'
