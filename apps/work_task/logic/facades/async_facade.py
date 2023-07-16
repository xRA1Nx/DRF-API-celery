from celery.result import AsyncResult
from apps.work_task.tasks import work_task__start__task, work_task__finish__task


def async__work_task__start(*, work_task_pk: int) -> AsyncResult:
    return work_task__start__task.delay(work_task_pk=work_task_pk)


def async__work_task__finish(*, work_task_pk: int) -> AsyncResult:
    return work_task__finish__task.delay(work_task_pk=work_task_pk)
