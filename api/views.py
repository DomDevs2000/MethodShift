from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class TaskList(APIView):
    def get(self, request: Request) -> Response:
        task: Task = Task.objects.all()
        serializer: TaskSerializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request: Request)-> Response:
        serializer: TaskSerializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):

    def get_object(self, pk: int) -> any:
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int) -> Response:
        task = self.get_object(pk)
        serializer: TaskSerializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        task: Task = self.get_object(pk)
        serializer: TaskSerializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
