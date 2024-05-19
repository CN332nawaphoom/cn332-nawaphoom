from django.contrib import admin
from .models import Task, Task_process

# Register your models here.
admin.site.register(Task)
admin.site.register(Task_process)