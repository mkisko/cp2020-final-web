from django.contrib import admin
from .models import *

admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Regulations)
admin.site.register(Comment)

admin.site.register(Role)
admin.site.register(Profile)

admin.site.register(Question)
admin.site.register(Answer)