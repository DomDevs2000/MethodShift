from typing import TypeAlias
from rest_framework import serializers
from .models import Task
import logging

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model: TypeAlias = Task
        fields: list[str] = ["id","task_name", "start_date","end_date", "cycle_time"]
        
    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        if end_date < start_date:
            raise serializers.ValidationError('End date cannot be before start date')
        return data
