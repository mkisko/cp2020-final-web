from django.contrib import admin
from .models import *

admin.site.register(Task)
admin.site.register(Comment)

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Answer)