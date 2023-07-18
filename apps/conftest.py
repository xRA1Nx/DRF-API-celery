import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture()
def api_client__super_user_factory__auth(api_client, super_user_factory):
    api_client.force_authenticate(user=super_user_factory())
    return api_client
