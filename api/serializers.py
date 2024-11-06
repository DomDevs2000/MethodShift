from typing import TypeAlias
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model: TypeAlias = Task
        fields: list[str] = ["task_name", "start_date","end_date", "cycle_time"]
