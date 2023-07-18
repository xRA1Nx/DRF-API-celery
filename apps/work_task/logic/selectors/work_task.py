import datetime

from django.db.models import QuerySet

from apps.work_task.models import WorkTask


def work_tasks__none() -> QuerySet[WorkTask]:
    return WorkTask.objects.none()


def work_tasks__all() -> QuerySet[WorkTask]:
    return WorkTask.objects.all()


def work_task__find_by_pk(
        *,
        pk: int,
        qs: QuerySet[WorkTask] | None = None,
) -> WorkTask | None:
    if qs is None:
        qs = work_tasks__all()
    return qs.filter(pk=pk).first()


def work_task__after_current_datetime(
        *,
        date_time: datetime.time,
        qs: QuerySet[WorkTask] | None = None,
) -> QuerySet[WorkTask]:
    if qs is None:
        qs = work_tasks__all()
    return qs.filter(finished_at__gte=date_time)
