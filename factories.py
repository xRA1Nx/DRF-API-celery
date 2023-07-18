from __future__ import annotations

from pytest_factoryboy import register

from apps.users.tests.factories import UserFactory
from apps.work_task.tests.factories import WorkTaskFactory

register(UserFactory)
register(WorkTaskFactory)
