from django import template
from main.models import Task

register = template.Library()

@register.filter
def progress(task):
    subtasks = task.subtasks.all()

    if subtasks.count() > 0:
        return int(subtasks.filter(success=True).count() / subtasks.count() * 100) 
    elif task.status == 'ended':
        return 100 
    
    return 0