from django.urls import path
from .views import *

urlpatterns = [
    path('voice/parser/', VioceParser.as_view(), name='voice-parser')
]