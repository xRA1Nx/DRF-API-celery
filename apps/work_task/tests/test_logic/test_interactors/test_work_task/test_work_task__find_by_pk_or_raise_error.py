import pytest
from restdoctor.rest_framework.exceptions import BusinessLogicException

from apps.work_task.constant.message import WORK_TASK_DOES_NOT_EXIST
from apps.work_task.logic.interactors.work_task import work_task__find_by_pk_or_raise_error
from apps.work_task.logic.selectors.work_task import work_tasks__none


def test__work_task__find_by_pk_or_raise_error__success_case(
        mocked__work_task__find_by_pk,
):
    pk = 100500
    expected_work_task = 'any_not_empty_data_any_type'
    mocked__work_task__find_by_pk.return_value = expected_work_task

    test_result = work_task__find_by_pk_or_raise_error(pk=pk)

    assert test_result == expected_work_task

def test__work_task__find_by_pk_or_raise_error__error_case(
        mocked__work_task__find_by_pk,
):
    pk = 100500
    expected_work_task = work_tasks__none()
    mocked__work_task__find_by_pk.return_value = expected_work_task

    with pytest.raises(BusinessLogicException, match=WORK_TASK_DOES_NOT_EXIST):
        test_result = work_task__find_by_pk_or_raise_error(pk=pk)


