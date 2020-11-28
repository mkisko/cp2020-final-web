from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    person = models.ManyToManyField(User, related_name='tasks')

    STATUS = [
        ('free', 'Свободная'),
        ('active', 'Активная'),
        ('process', 'В процессе'),
        ('ended', 'Завершена')
    ]
    status = models.CharField(max_length=10, choices=STATUS, default='free')

    hours = models.IntegerField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    fio = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    hours_per_day = models.IntegerField(default=8)

class Question(models.Model):
    title = models.CharField(max_length=255)

class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)