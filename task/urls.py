from django.urls import path
from .views import ListTask, CreateTask, DeleteTask,UpdateTask,ListCreateSubTask,RetrieveUpdateDestroySubTask

urlpatterns = [
    path('',ListTask.as_view(),name="list_task"),
    path('create/',CreateTask.as_view(),name="create_task"),
    path('delete/<int:pk>',DeleteTask.as_view(),name="delete_task"),
    path('update/<int:pk>', UpdateTask.as_view(), name="update_task"),
    path('sub-task/',ListCreateSubTask.as_view(),name="list_create_subtask"),
    path('sub-task/<int:pk>',RetrieveUpdateDestroySubTask.as_view(), name='retrieve_update_destroy_sub-task')
]
