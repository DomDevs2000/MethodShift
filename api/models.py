from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.
class CycleTime(models.Model):
    task_name: CharField = models.CharField(max_length=255)
    start_date = models.DateField
    end_date = models.DateField

    #TODO: Cycle time 

    def __str__(self):
        return self.task_name
