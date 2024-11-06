from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

# test view
# def index(request):
#     return HttpResponse('hello')


# django rest framework view
class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class =  TaskSerializer
