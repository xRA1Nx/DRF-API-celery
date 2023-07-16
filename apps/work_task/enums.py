from django.db import models


class TaskChoices(models.TextChoices):
    CREATED = 'created', 'created'
    STARTED = 'started', 'started'
    FINISHED = 'finished', 'finished'
