from django.urls import path
from .import views

urlpatterns = [
    path('' , views.apiOverview , name="apiOverview"),
    path('task-list/' , views.TaskList , name='Task List'),
    path('task-create/' , views.TaskCreate , name = 'Task Create')
]
