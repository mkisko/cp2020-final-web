from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),

    #map
    path('map/', Map.as_view(), name="map-index"),

    # kanban
    path('kanban/', Kanban.as_view(), name='kanban-index'),
    path('kanban/create/', KanbanForm.as_view(), name='kanban-create'),
    path('kanban/<int:id>/edit/', KanbanForm.as_view(), name='kanban-edit'),
    path('kanban/<int:id>/view/', KanbanView.as_view(), name='kanban-view'),
    path('kanban/<int:id>/delete/', KanbanView.as_view(), name='kanban-delete'),
]