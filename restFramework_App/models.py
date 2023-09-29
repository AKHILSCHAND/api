from django.db import models

# Create your models here.


class Task(models.Model):
    task_name=models.CharField(max_length=150)
    task_description=models.CharField(max_length=250)
    task_completed = models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    