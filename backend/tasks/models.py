from django.db import models
from employees.models import Employee

class Task(models.Model):
    title = models.CharField(unique=True,max_length=200)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name='tasks')
    creation_date = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
          return self.title