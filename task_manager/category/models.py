from django.db import models
from task.models import TaskModel

# Create your models here.
class TaskCategory(models.Model):
    category_name=models.CharField(max_length=100)
    tasks=models.ManyToManyField(TaskModel)

    

    def __str__(self):
        return self.category_name
