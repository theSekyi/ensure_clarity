from rest_framework import generics
from .models import Task, SubTask
from .serializers import TaskSerializer,SubTaskSerializer


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

class ListCreateSubTask(generics.ListCreateAPIView):
    queryset =  SubTask.objects.all()
    serializer_class = SubTaskSerializer

class RetrieveUpdateDestroySubTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer