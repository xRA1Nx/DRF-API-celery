from __future__ import annotations

from django.db import models


class AbstractMainModel(models.Model):
    """
    Общий шаблон для наследования моделей.
    """

    class Meta:
        abstract = True

    is_active = models.BooleanField(
        verbose_name='активный', default=True,
    )
    is_available = models.BooleanField(
        verbose_name='доступный', default=True
    )
    created_at = models.DateTimeField(
        verbose_name='дата и время создания', auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='дата и время изменения', auto_now=True
    )
