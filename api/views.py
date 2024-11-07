from webbrowser import get
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas.coreapi import serializers

from .models import Task
from .serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def get_all_tasks(request)-> Response:
    tasks: Task = Task.objects.all()
    serializer: TaskSerializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_task(request,pk)-> Response:
    try:
        task: Task = Task.objects.get(pk=pk)
        serializer: TaskSerializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET','PUT','DELETE'])
def tasks(request,pk)-> Response:
    try:
        task: Task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer: TaskSerializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer: TaskSerializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_task(request)-> Response:
    serializer = TaskSerializer(date=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['PUT'])
# def update_task(request, pk)-> Response:
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = TaskSerializer(date=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['DELETE'])
# def delete_task(request, pk)-> Response:
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     task.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
