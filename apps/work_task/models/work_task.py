from apps.work_task.enums import TaskChoices
from common.models.main_abstract import AbstractMainModel
from django.db import models


class WorkTask(AbstractMainModel):
    class Meta:
        verbose_name = 'Рабочая задача'
        verbose_name_plural = 'Рабочая задача'

    status = models.CharField(
        verbose_name='статус',
        choices=TaskChoices.choices,
        default=TaskChoices.CREATED,
        max_length=10
    )

    finished_at = models.DateTimeField(
        null=True,
        blank=True
    )
