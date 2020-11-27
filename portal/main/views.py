from django.shortcuts import render
from django.views import View

from .models import Task
class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

class Kanban(View):
    def get(self, request):
        tasks = Task.objects.all()

        return render(request, 'kanban/index.html', {
            'tasks': tasks
        })