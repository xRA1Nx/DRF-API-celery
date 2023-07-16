from django.utils.timezone import localtime
from restdoctor.rest_framework.exceptions import BusinessLogicException

from apps.work_task.constant.message import WORK_TASK_IS_NOT_STARTED, WORK_TASK_IS_NOT_CREATED, WORK_TASK_DOES_NOT_EXIST
from apps.work_task.enums import TaskChoices
from apps.work_task.logic.selectors.work_task import work_task__find_by_pk
from apps.work_task.models import WorkTask
from common.logic.interactors.common import update_model_instance


def work_task__check_status_before_finish(*, work_task: WorkTask) -> None:
    if work_task.status != TaskChoices.STARTED:
        raise BusinessLogicException(WORK_TASK_IS_NOT_STARTED)


def work_task__check_status_before_start(*, work_task: WorkTask) -> None:
    if work_task.status != TaskChoices.CREATED:
        raise BusinessLogicException(WORK_TASK_IS_NOT_CREATED)


def work_task__find_by_pk_or_raise_error(*, pk: int) -> WorkTask:
    work_task = work_task__find_by_pk(pk=pk)
    if not work_task:
        raise BusinessLogicException(WORK_TASK_DOES_NOT_EXIST)
    return work_task


def work_task__start(*, work_task_pk: int) -> None:
    work_task = work_task__find_by_pk(pk=work_task_pk)
    update_model_instance(
        instance=work_task,
        validated_data={
            'status': TaskChoices.STARTED
        },
        update_fields=['status', ]
    )


def work_task__finish(*, work_task_pk: int) -> None:
    work_task = work_task__find_by_pk(pk=work_task_pk)
    # бизнес логика не определена, тут можно логировать , или обрабатывать ошибку
    if not work_task:
        return

    update_model_instance(
        instance=work_task,
        validated_data={
            'status': TaskChoices.FINISHED,
            'finished_at': localtime()
        },
        update_fields=['status', 'finished_at']
    )
