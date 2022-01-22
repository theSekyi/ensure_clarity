from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer


class ListTask(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateTask(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTask(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTask(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer