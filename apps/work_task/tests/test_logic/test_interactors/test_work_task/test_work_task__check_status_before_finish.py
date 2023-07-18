import pytest
from restdoctor.rest_framework.exceptions import BusinessLogicException

from apps.work_task.constant.message import WORK_TASK_IS_NOT_STARTED
from apps.work_task.enums import TaskChoices
from apps.work_task.logic.interactors.work_task import work_task__check_status_before_finish


@pytest.mark.django_db()
def test__work_task__check_status_before_finish__success_case(
        work_task_factory
):
    work_task = work_task_factory(status=TaskChoices.STARTED)

    work_task__check_status_before_finish(work_task=work_task)


@pytest.mark.parametrize('status', [TaskChoices.FINISHED, TaskChoices.CREATED])
@pytest.mark.django_db()
def test__work_task__check_status_before_finish__error_case(
        work_task_factory, status
):
    work_task = work_task_factory(status=status)

    with pytest.raises(BusinessLogicException, match=WORK_TASK_IS_NOT_STARTED):
        work_task__check_status_before_finish(work_task=work_task)
