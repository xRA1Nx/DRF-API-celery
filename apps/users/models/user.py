import uuid as uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from apps.users.managers import UserManager
from common.models.main_abstract import AbstractMainModel
from django.db import models


class User(AbstractMainModel, AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions: list[str] = []

    USERNAME_FIELD = 'login'

    objects = UserManager()

    login = models.CharField(
        verbose_name='логин',
        max_length=255,
        db_index=True,
        unique=True,

    )
    first_name = models.CharField(
        verbose_name='имя',
        max_length=255,
    )
    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=255,
        db_index=True,
    )
    middle_name = models.CharField(  # null_for_compatibility
        verbose_name='отчество',
        max_length=255,
        null=True,
        blank=True,
    )
    email = models.EmailField(
        verbose_name='адрес электронной почты',
        max_length=255,
        unique=True,
    )

    is_staff = models.BooleanField(
        verbose_name='статус персонала',
        default=False,
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
