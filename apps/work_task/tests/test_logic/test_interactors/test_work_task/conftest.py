from unittest.mock import Mock

import pytest

@pytest.fixture
def mocked__update_model_instance(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.interactors.work_task',
        function_name='update_model_instance',
    )



@pytest.fixture
def mocked__work_task__find_by_pk(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.interactors.work_task',
        function_name='work_task__find_by_pk',
    )



