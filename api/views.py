from django.shortcuts import render
from rest_framework import generics
from .models import CycleTime
from .serializers import CycleTimeSerialzer

# Create your views here.


# def index(request):
#     return HttpResponse('hello')
class CycleTimeListCreate(generics.ListCreateAPIView):
    queryset = CycleTime.objects.all()
    serializer_class =  CycleTimeSerialzer
