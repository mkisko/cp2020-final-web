from django import template
from main.models import Answer

register = template.Library()

@register.filter
def answer(question, profile):
    return Answer.objects.filter(question=question, user=profile.user).first()

@register.filter
def workload(profile):
    time = 0

    for task in profile.user.tasks.all():
        time += task.hours

    return int(time / profile.hours_per_day * 100)