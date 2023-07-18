from apps.work_task.enums import TaskChoices
from apps.work_task.logic.interactors.work_task import work_task__start


def test__work_task__start(
        mocked__update_model_instance,
        mocked__work_task__find_by_pk,
):
    expected_pk = 100500
    expected_work_task = 'any'
    mocked__work_task__find_by_pk.return_value = expected_work_task

    work_task__start(work_task_pk=expected_pk)

    mocked__update_model_instance.assert_called_once_with(
        instance=expected_work_task,
        validated_data={'status': TaskChoices.STARTED},
        update_fields=['status']
    )
