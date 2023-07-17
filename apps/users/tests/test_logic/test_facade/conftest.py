from unittest.mock import Mock

import pytest


@pytest.fixture
def mocked__create_model_instance(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.users.logic.facades.user',
        function_name='create_model_instance',
    )
