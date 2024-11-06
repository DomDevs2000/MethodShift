from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.CycleTimeListCreate.as_view(), name="test view"),
]
