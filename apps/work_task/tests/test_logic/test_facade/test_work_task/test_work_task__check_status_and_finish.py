import pytest

from apps.work_task.logic.facades.work_task import work_task__check_status_and_finish


@pytest.mark.django_db()
def test__work_task__check_status_and_finish(
        work_task,
        mocked__work_task__find_by_pk_or_raise_error,
        mocked__work_task__check_status_before_finish,
        mocked__async__work_task__finish,
):
    work_task_pk = 100500
    mocked__work_task__find_by_pk_or_raise_error.return_value = work_task

    work_task__check_status_and_finish(work_task_pk=work_task_pk)

    mocked__work_task__find_by_pk_or_raise_error.assert_called_once_with(pk=work_task_pk)
    mocked__work_task__check_status_before_finish.assert_called_once_with(work_task=work_task)
    mocked__async__work_task__finish.assert_called_once_with(work_task_pk=work_task_pk)
