from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from .models import Task, Question, Profile
from .forms import TaskForm
class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

@method_decorator(csrf_exempt, name='dispatch')
class Kanban(View):
    def get(self, request):
        tasks = Task.objects.all()

        return render(request, 'kanban/index.html', {
            'kanban': {
                'Сободные': tasks.filter(status='free'),
                'Активные': tasks.filter(status='active'),
                'В процессе': tasks.filter(status='process'),
                'Завершенные': tasks.filter(status='ended')
            }
        })

    def post(self, request):
        data = request.POST

        task = Task.objects.get(id=data['id'])
        task.status = data['status']
        task.save()

        return HttpResponse()
class KanbanView(View):
    def get(self, request, id):
        task = Task.objects.get(id=id)

        return render(request, 'kanban/view.html', {
            'task': task
        })

    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()

        return redirect('kanban-index')  
class KanbanForm(View):
    def get(self, request, id=None):
        form = TaskForm() if not id else TaskForm(instance=Task.objects.get(id=id))

        return render(request, 'kanban/form.html', {
            'form': form
        })

    def post(self, request, id=None):
        form = TaskForm(request.POST, instance=None if not id else Task.objects.get(id=id))

        if form.is_valid():
            form.save()

            return redirect('kanban-index') if not id else redirect('kanban-view', id)

        return render(request, 'kanban/form.html', {
            'form': form
        })

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