from typing import Any
from django.db import models
from django import forms
from django.contrib.auth.models import User
from . import Factory
import json


# Create your models here.
class Task(models.Model):
    # information
    intersection_name = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # video
    video = models.FileField(upload_to='videos/')


    def detect(self,name_model,coordinate):
        model = Factory.get_model(name_model)
        if model != None:
            data = model.detect(self.video.path,coordinate)
            return data
    
    def get_video_name(self):
        return self.video.path
    
    def __str__(self):
        return self.intersection_name
    

class Task_process(models.Model):
    
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    # video
    detected_vdo = models.FileField(upload_to='result/')

    extra_data = models.TextField() 
    
    def get_data(self):
        # Deserialize JSON data from the extra_data field
        return json.loads(self.extra_data)

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'intersection_name',
            'province',
            'video',
        ]
        labels = {
            'intersection_name': "Intersection Name",
            'province': 'Province',
            'video': 'Video'
        }

        widgets = {
            'intersection_name': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
        }

