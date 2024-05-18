from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='index'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/upload_video/', views.upload_video, name='upload_video'),
    path('dashboard/task/<int:id>', views.task_info, name="task_info"),
    path('dashboard/task_process/<int:id>', views.process_info, name="process_info"),
    path('process/task/<int:id>', views.process, name="process"),
    path('dashboard/task/delete/<int:id>', views.delete_task, name="delete_task"),
]
