from django.utils.timezone import localtime
from freezegun import freeze_time

from apps.work_task.enums import TaskChoices
from apps.work_task.logic.interactors.work_task import work_task__start, work_task__finish


def test__work_task__work_task__finish__success_case(
        mocked__update_model_instance,
        mocked__work_task__find_by_pk,
):
    expected_pk = 100500
    expected_time = localtime()
    expected_work_task = 'any'
    mocked__work_task__find_by_pk.return_value = expected_work_task

    with freeze_time(expected_time):
        work_task__finish(work_task_pk=expected_pk)

    mocked__update_model_instance.assert_called_once_with(
        instance=expected_work_task,
        validated_data={
            'status': TaskChoices.FINISHED,
            'finished_at': expected_time,
        },
        update_fields=['status', 'finished_at']
    )


def test__work_task__work_task__finish__case_not_work_task(
        mocked__update_model_instance,
        mocked__work_task__find_by_pk,
):
    expected_pk = 100500
    mocked__work_task__find_by_pk.return_value = None

    work_task__finish(work_task_pk=expected_pk)

    mocked__update_model_instance.assert_not_called()
