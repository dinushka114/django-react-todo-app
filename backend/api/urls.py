from django.urls import path
from .import views

urlpatterns = [
    path('' , views.apiOverview , name="apiOverview"),
    path('task-list/' , views.TaskList , name='Task List'),
    path('task-create/' , views.TaskCreate , name = 'Task Create'),
    path('task-detail/<str:pk>/' , views.TaskDetail , name = 'Task Detail'),
    path('task-update/<str:pk>' , views.TaskUpdate , name = 'Task Update'),
    path('task-delete/<str:pk>' , views.TaskDelete , name="Task Delete")
]
