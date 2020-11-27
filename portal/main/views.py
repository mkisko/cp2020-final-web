from django.shortcuts import render
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'main/index.html')

def test(request):
    return render(request, 'main/test.html')

def kanban(request):
    return render(request, 'kanban/index.html')