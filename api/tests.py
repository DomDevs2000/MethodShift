import datetime
from django.test import TestCase
from .models import Task

# Create your tests here.

class TaskModelTest(TestCase):

    #Tests whether the cycle time is calculated correctly
    def test_cycle_time(self):
        start_date = datetime.datetime(2022, 1, 1, 12, 0, 0)
        end_date = datetime.datetime(2022, 1, 3, 14, 30, 0)
        task = Task(task_name="Test Task", start_date=start_date, end_date=end_date)
        
        self.assertEqual(task.cycle_time, "2 days, 2 hours, 30 minutes")

