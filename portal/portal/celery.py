import os
import datetime

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

app = Celery('portal', broker=os.getenv('BROKER_CELERY'))
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'clear_last_day_answers': {
        'task': 'main.tasks.clear_last_day_answers',
        'schedule': crontab()
    }
}