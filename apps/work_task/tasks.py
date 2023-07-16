import datetime
import typing

from celery import shared_task
from django.utils.timezone import localtime

from apps.work_task.logic.interactors.work_task import work_task__start, work_task__finish
from apps.work_task.logic.selectors.work_task import work_task__after_current_datetime


@shared_task
def work_task__start__task(*, work_task_pk: int):
    return work_task__start(work_task_pk=work_task_pk)


@shared_task
def work_task__finish__task(*, work_task_pk: int):
    return work_task__finish(work_task_pk=work_task_pk)


@shared_task
def finished_work_task__db_cleaner__task():
    return finished_work_task__db_cleaner()


def finished_work_task__db_cleaner():
    time_now = localtime()
    weak_before = time_now - datetime.timedelta(days=7)
    qs = work_task__after_current_datetime(date_time=weak_before)
    qs.delete()
