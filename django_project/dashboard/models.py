from django.db import models
from django import forms

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
    

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

