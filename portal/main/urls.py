from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),

    #map
    path('map/', Map.as_view(), name="map-index"),

    #employees
    path('employees/', Employee.as_view(), name="employee"),

    # kanban
    path('kanban/', Kanban.as_view(), name='kanban'),

    # security


]