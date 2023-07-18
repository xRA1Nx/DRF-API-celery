from factory import Sequence
from factory.django import DjangoModelFactory
from faker import Faker

from apps.users.models import User
from apps.work_task.enums import TaskChoices
from apps.work_task.models import WorkTask

fake = Faker()


class WorkTaskFactory(DjangoModelFactory):
    class Meta:
        model = WorkTask

