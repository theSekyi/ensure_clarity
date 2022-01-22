from django.urls import path
from .views import ListTask, CreateTask, DeleteTask,UpdateTask

urlpatterns = [
    path('',ListTask.as_view(),name="list_task"),
    path('create/',CreateTask.as_view(),name="create_task"),
    path('delete/<int:pk>',DeleteTask.as_view(),name="delete-task"),
    path('update/<int:pk>', UpdateTask.as_view(), name="update-task")
]
