from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('tasks/list/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:id>/', TaskList.as_view(), name='task-view'),

    path('voice/parser/', VioceParser.as_view(), name='voice-parser'),
    path('regulation/get/', GetRegulation.as_view(), name='regulation')
]