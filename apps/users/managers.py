from __future__ import annotations

import typing


from django.contrib.auth.base_user import BaseUserManager

if typing.TYPE_CHECKING:  # фикс кросс импорта
    from apps.users.models.user import User


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login: str, password: str | None) -> User:
        if not login:
            raise ValueError('У пользователя должен быть login')
        user = self.model(login=login)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login: str, password: str) -> User:
        user = self.create_user(login, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
