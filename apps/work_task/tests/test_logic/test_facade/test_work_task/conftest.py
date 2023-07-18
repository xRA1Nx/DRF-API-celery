from unittest.mock import Mock

import pytest


@pytest.fixture
def mocked__create_model_instance(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.facades.work_task',
        function_name='create_model_instance',
    )


@pytest.fixture
def mocked__work_task__find_by_pk_or_raise_error(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.facades.work_task',
        function_name='work_task__find_by_pk_or_raise_error',
    )


@pytest.fixture
def mocked__work_task__check_status_before_start(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.facades.work_task',
        function_name='work_task__check_status_before_start',
    )


@pytest.fixture
def mocked__async__work_task__start(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.facades.work_task',
        function_name='async__work_task__start',
    )


@pytest.fixture
def mocked__work_task__check_status_before_finish(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.facades.work_task',
        function_name='work_task__check_status_before_finish',
    )


@pytest.fixture
def mocked__async__work_task__finish(mock_for_module) -> Mock:
    return mock_for_module(
        module_name='apps.work_task.logic.facades.work_task',
        function_name='async__work_task__finish',
    )
