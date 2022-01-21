from django.urls import path
from views import ListTasks, CreateTasks

urlpatterns = [
    path('',ListTasks.as_view(),name="list_tasks"),
    path('create/',CreateTasks.as_view(),name="create_tasks")
]
