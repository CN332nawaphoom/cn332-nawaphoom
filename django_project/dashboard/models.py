from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title


