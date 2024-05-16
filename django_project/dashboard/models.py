from django.db import models
from django import forms
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.intersection_name
    

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

