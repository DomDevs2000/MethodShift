from django.db import models
from datetime import timedelta
from django.db.models.fields import CharField, DateField

# Create your models here.
class Task(models.Model):
    task_name: CharField = models.CharField(max_length=255)
    start_date: DateField = models.DateTimeField()
    end_date: DateField = models.DateTimeField()

    #TODO: Cycle time

    @property
    def cycle_time(self)-> str:
        delta: timedelta = self.end_date - self.start_date
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        return f"{days} days, {hours} hours, {minutes} minutes"

    def __str__(self)-> str:
        return str(self.task_name)
    
