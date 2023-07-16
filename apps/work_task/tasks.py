import typing
from time import localtime

from celery import shared_task

from apps.work_task.logic.interactors.work_task import work_task__start, work_task__finish


@shared_task
def work_task__start__task(*, work_task_pk: int):
    return work_task__start(work_task_pk=work_task_pk)


@shared_task
def work_task__finish__task(*, work_task_pk: int):
    return work_task__finish(work_task_pk=work_task_pk)


@shared_task
def finished_work_task__db_cleaner__task(*, work_task_pks: typing.Iterable[int]):
    return finished_work_task__db_cleaner()


def finished_work_task__db_cleaner():
    time_now = localtime()