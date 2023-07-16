from django.db.models import QuerySet

from apps.work_task.models import WorkTask


def work_task__none() -> QuerySet[WorkTask]:
    return WorkTask.objects.none()


def work_task__all() -> QuerySet[WorkTask]:
    return WorkTask.objects.all()


def work_task__find_by_pk(
        *,
        pk: int,
        qs: QuerySet[WorkTask] | None = None,
) -> WorkTask | None:
    if qs is None:
        qs = work_task__all()
    return qs.filter(pk=pk).first()


