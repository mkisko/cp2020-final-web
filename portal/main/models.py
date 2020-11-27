from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    person = models.ManyToManyField(User, related_name='tasks')

    STATUS = [
        (0, 'Свободная'),
        (1, 'Активная'),
        (2, 'В процессе'),
        (3, 'Завершена')
    ]
    status = models.IntegerField(choices=STATUS, default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
