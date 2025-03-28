from django.db import models
# from category.models import TaskCategory

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField(auto_now_add=True)
    # category=models.ForeignKey(TaskCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.taskTitle