import pytest
from rest_framework.test import APIClient # new import
import datetime
from api.models import Task
@pytest.fixture
def task() -> Task:
    return Task.objects.create(
        task_name="Test Task",
        start_date="2000-05-20T00:00:00Z",
        end_date="2000-07-20T00:00:00Z",
    )

    # Task.objects.create(
    #     task_name="Test Task 2",
    #     start_date="2000-05-20T00:00:00Z",
    #     end_date="2000-07-20T00:00:00Z",
    # )
   
@pytest.fixture()
def api_client() -> APIClient:  
     """  
     Fixture to provide an API client  
     """  
     yield APIClient()

@pytest.fixture
def task_payload() -> dict: # uses the user fixture
    return {
    "task_name": "test",
    "start_date": "2000-05-20T00:00:00Z",
    "end_date": "2000-07-20T00:00:00Z",
     }
