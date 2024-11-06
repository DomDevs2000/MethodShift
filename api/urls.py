from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.TaskListCreate.as_view(), name="test view"),
]
