from apps.work_task.logic.facades.async_facade import async__work_task__start, async__work_task__finish
from apps.work_task.logic.interactors.work_task import work_task__check_status_before_start, \
    work_task__find_by_pk_or_raise_error, work_task__check_status_before_finish
from apps.work_task.models import WorkTask
from common.logic.interactors.common import create_model_instance


def work_task__period(*, work_task: WorkTask) -> int:
    created_at = work_task.created_at
    finished_at = work_task.finished_at
    if not created_at or not finished_at:
        return 0
    return finished_at - created_at


def work_task__create() -> WorkTask:
    return create_model_instance(
        model_class=WorkTask,
        validated_data={}
    )


def work_task__check_status_and_start(*, work_task_pk: int) -> None:
    work_task = work_task__find_by_pk_or_raise_error(pk=work_task_pk)
    work_task__check_status_before_start(work_task=work_task)
    async__work_task__start(work_task_pk=work_task_pk)


def work_task__check_status_and_finish(*, work_task_pk: int) -> None:
    work_task = work_task__find_by_pk_or_raise_error(pk=work_task_pk)
    work_task__check_status_before_finish(work_task=work_task)
    async__work_task__finish(work_task_pk=work_task_pk)


