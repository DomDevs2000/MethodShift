from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name="task"),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name="task-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
