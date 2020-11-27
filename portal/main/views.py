from django.shortcuts import render, redirect
from django.views import View

from .models import Task
from .forms import TaskForm
class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

class Kanban(View):
    def get(self, request):
        tasks = Task.objects.all()

        return render(request, 'kanban/index.html', {
            'tasks': tasks
        })

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

        return render(request, 'kanban/create.html', {
            'form': form
        })

    def post(self, request, id=None):
        form = TaskForm(request.POST, instance=None if not id else Task.objects.get(id=id))

        if form.is_valid():
            form.save()

            return redirect('kanban-index') if not id else redirect('kanban-view', id)

        return render(request, 'kanban/create.html', {
            'form': form
        })
