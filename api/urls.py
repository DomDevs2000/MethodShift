from django.urls import path

from .views import get_all_tasks, create_task, tasks

urlpatterns = [
    path("tasks/", get_all_tasks, name="get_all_tasks"),
    path("tasks/<int:pk>", tasks, name="tasks"),
    path("tasks/create", create_task, name="create_task"),
]
