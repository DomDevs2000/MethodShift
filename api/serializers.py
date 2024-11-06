from rest_framework import serializers
from .models import CycleTime

class CycleTimeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CycleTime
        fields = ["task_name", "start_date","end_date"]
