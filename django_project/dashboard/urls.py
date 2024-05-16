from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='index'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/upload_video/', views.upload_video, name='upload_video')
]