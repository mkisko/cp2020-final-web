from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Task, Question, Profile
from .forms import TaskForm
class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class Kanban(View):
    def get(self, request):
        tasks = Task.objects.all()
        users = User.objects.all()

        return render(request, 'main/kanban.html', {
            'kanban': {
                'Сободные': tasks.filter(status='free'),
                'Активные': tasks.filter(status='active'),
                'В процессе': tasks.filter(status='process'),
                'Завершенные': tasks.filter(status='ended')
            },
            'users': users
        })

    def post(self, request):
        data = request.POST
        type = data.get('type')

        if type == 'get':
            task = Task.objects.get(id=request.GET.get('id'))

            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'hours': task.hours,
                'author': task.author.id,
                'persons': [person.id for person in task.person.all()],
                'comments': [{'text': comment.text, 'user': comment.user.id} for comment in task.comments.all()]
            })
        
        elif type == 'delete':
            task = Task.objects.get(id=request.GET.get('id'))
            task.delete()
            messages.error(request, 'Задача удалена!')

            return redirect('kanban')
        
        else:
            form = TaskForm(request.POST, instance=None if not request.GET.get('id') else Task.objects.get(id=request.GET.get('id')))
            if form.is_valid():
                form.save()
                messages.success(request, 'Задача успешно обновлена!')
            else:
                messages.error(request, 'Произошла ошибка при сохранении!')
        
        return redirect('kanban')

class Map(View):
    def get(self, request):
        return render(request, 'map/index.html')

class Employee(View):
    def get(self, request):
        profile = Profile.objects.all()
        questions = Question.objects.all()

        return render(request, 'employees/index.html', {
            'profiles': profile,
            'questions': questions
        })
