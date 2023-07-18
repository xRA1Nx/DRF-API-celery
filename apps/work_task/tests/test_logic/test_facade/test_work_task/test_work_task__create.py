import pytest

from apps.work_task.logic.facades.work_task import work_task__create
from apps.work_task.models import WorkTask


@pytest.mark.django_db()
def test__work_task__create(mocked__create_model_instance):
    work_task__create()

    mocked__create_model_instance.assert_called_once_with(
        model_class=WorkTask,
        validated_data={},
    )
