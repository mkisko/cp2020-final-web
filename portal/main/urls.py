from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),

    #map
    path('map/', Map.as_view(), name="map"),

    #employees
    path('employeers/', Employeers.as_view(), name="employeers"),
    path('employeers/<int:id>/', Employeers.as_view(), name="employeer-view"),

    # kanban
    path('kanban/', Kanban.as_view(), name='kanban'),

    # security
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),  name='logout'),
]