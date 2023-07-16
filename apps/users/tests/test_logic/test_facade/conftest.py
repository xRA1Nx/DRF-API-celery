from unittest.mock import Mock

import pytest


@pytest.fixture
def mocked__user__create(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.users.logic.facades.user',
        function_name='user__create',
    )
