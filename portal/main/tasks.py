from portal.celery import app
from datetime import datetime, timedelta
from django.utils import timezone

from .models import Answer

@app.task
def clear_last_day_answers():
    Answer.objects.filter(created__lt=timezone.now() - timedelta(days=1)).delete()
