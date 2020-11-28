from django.db import models
from django.contrib.auth.models import User

# USER MODELS
class Role(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    skills = models.TextField(blank=True, verbose_name='Навыки')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')

    fio = models.CharField(max_length=50, verbose_name='ФИО')
    role = models.ForeignKey(Role, related_name='profiles', on_delete=models.CASCADE, verbose_name='Роль в системе')
    hours_per_day = models.IntegerField(default=8, verbose_name='Часов в день', help_text='Количество часов в день которое может отрабатывать работник')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

# TASK & TEMPLATES
class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    person = models.ManyToManyField(User, related_name='tasks', blank=True, verbose_name='Ответственные за выполнение')

    STATUS = [
        ('free', 'Свободная'),
        ('active', 'Активная'),
        ('process', 'В процессе'),
        ('ended', 'Завершена')
    ]
    status = models.CharField(max_length=10, choices=STATUS, default='free', verbose_name='Статус задачи')

    PRIORITY = [
        ('base', 'Обычная'),
        ('important', 'Важная'),
        ('hot', 'Срочная')
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY, default='base', verbose_name='Приоритет задачи')

    hours = models.IntegerField(verbose_name='Часов на реализацию')
    author = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE, verbose_name='Создатель задачи')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class SubTask(models.Model):
    task = models.ForeignKey(Task, related_name='subtasks', on_delete=models.CASCADE, verbose_name='Задача')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    hours = models.IntegerField(verbose_name='Часов на реализацию')
    success = models.BooleanField(default=False, verbose_name='Задача выполнена')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'
class Regulations(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    roles = models.ManyToManyField(Role, related_name='regulations', blank=True, verbose_name='Компетенции')
    hours = models.IntegerField(verbose_name='Часов на реализацию')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Норматив'
        verbose_name_plural = 'Нормативы'

# SOME MODELS FOREIGN TASK
class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE, verbose_name='Задача')
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='Создатель')
    text = models.TextField(max_length=1000, verbose_name='Комментарий')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

# QUIZ FOR USERS
class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Текст вопроса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, verbose_name='Вопрос')
    answer = models.CharField(max_length=255, verbose_name='Ответ')

    def __str__(self):
        return self.answer
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'