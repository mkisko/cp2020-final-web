from django.db import models
from django.contrib.auth.models import User

# USER MODELS
class Role(models.Model):
    title = models.CharField(max_length=100)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.title    

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    fio = models.CharField(max_length=50)
    role = models.ForeignKey(Role, related_name='profiles', on_delete=models.CASCADE)
    hours_per_day = models.IntegerField(default=8)

    def __str__(self):
        return self.fio

# TASK & TEMPLATES
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    person = models.ManyToManyField(User, related_name='tasks', blank=True)

    STATUS = [
        ('free', 'Свободная'),
        ('active', 'Активная'),
        ('process', 'В процессе'),
        ('ended', 'Завершена')
    ]
    status = models.CharField(max_length=10, choices=STATUS, default='free')

    hours = models.IntegerField()
    author = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Regulations(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    roles = models.ManyToManyField(Role, related_name='regulations', blank=True)
    hours = models.IntegerField()

    def __str__(self):
        return self.title

# SOME MODELS FOREIGN TASK
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)


# QUIZ FOR USERS
class Question(models.Model):
    title = models.CharField(max_length=255)

class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)