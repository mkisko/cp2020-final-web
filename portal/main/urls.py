from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('kanban/', Kanban.as_view(), name='kanban-index'),
]