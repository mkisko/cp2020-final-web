import json
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Task, Question, Profile, SubTask
from .forms import TaskForm

@method_decorator(login_required, name='dispatch')
class Index(View):
    def get(self, request):
        return render(request, 'index.html')

@method_decorator(login_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class Kanban(View):
    def get(self, request):
        tasks = Task.objects.all()
        users = User.objects.all()

        return render(request, 'kanban.html', {
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
        
        # Get data for task
        # Return json(task)
        if type == 'get':
            task = Task.objects.get(id=request.GET.get('id'))

            return JsonResponse({
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'status': task.status,
                'priority': task.priority,
                'hours': task.hours,
                'author': task.author.id,
                'persons': [person.id for person in task.person.all()],
                'comments': [{'text': comment.text, 'user': comment.author.profile.fio} for comment in task.comments.all()],
                'subtasks': [{'id': sub.id, 'title': sub.title, 'hours': sub.hours, 'success': sub.success} for sub in task.subtasks.all()]
            })
        
        # Change status success for sub task
        # Return {'success': true/false}
        elif type == 'changeSubTask':
            try:
                sub = SubTask.objects.get(id=data.get('id'))
                sub.success = not sub.success
                sub.save()

                return JsonResponse({'success': True})
            except:
                return JsonResponse({'success': False})
        
        # Create sub task from request 
        # Return {'success': true/false, id: }
        elif type == 'createSubTask':
            try:
                sub = SubTask.objects.create(task=Task.objects.get(id=data.get('id')), title=data.get('title'), hours=data.get('hours'))
                return JsonResponse({'success': True, 'id': sub.id})
            except:
                return JsonResponse({'success': False})
        
        # Delete task
        # Return redirect
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
                messages.error(request, 'Произошла ошибка при сохранении! ' + json.dumps(form.errors))
        
        return redirect('kanban')

@method_decorator(login_required, name='dispatch')
class Map(View):
    def get(self, request):
        return render(request, 'map.html')

@method_decorator(login_required, name='dispatch')
class Employee(View):
    def get(self, request):
        profile = Profile.objects.all()
        questions = Question.objects.all()

        return render(request, 'employeers.html', {
            'profiles': profile,
            'questions': questions
        })
