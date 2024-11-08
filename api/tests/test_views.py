import pytest
from django.urls import reverse
from rest_framework import status
from api.views import TaskList

from api.models import Task
from api.serializers import TaskSerializer


# Checks two tasks created in conftest.py exist and their task names match
@pytest.mark.django_db
def test_get_all_tasks(api_client, task):

    url = reverse("task")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK

    tasks = Task.objects.all()
    expected_data = TaskSerializer(tasks, many=True).data

    assert response.data == expected_data
    assert len(response.data) == 1
    assert any(task["task_name"] == "Test Task" for task in response.data)
    # assert any(task['task_name'] == "Test Task 2" for task in response.data)


# checks that a new task was created
@pytest.mark.django_db
def test_create_task_view(api_client, task_payload):
    url = reverse("task")
    response = api_client.post(url, data=task_payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["task_name"] == task_payload["task_name"]
    assert response.data["start_date"] == task_payload["start_date"]
    assert response.data["end_date"] == task_payload["end_date"]
    assert Task.objects.filter(task_name=task_payload["task_name"]).exists()
