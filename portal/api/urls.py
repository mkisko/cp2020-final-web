from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('voice/parser/', VioceParser.as_view(), name='voice-parser'),
    path('regulation/get/', GetRegulation.as_view(), name='regulation')
]