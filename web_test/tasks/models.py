from django.db import models


class Date(models.Model):
    dt = models.DateField(unique=True)
    
    def __str__(self):
        return str(self.dt)
    

class Task(models.Model):
    task = models.CharField(max_length=100)
    dt = models.ForeignKey(Date, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
