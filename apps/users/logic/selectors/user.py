from django.db.models import QuerySet

from apps.users.models import User


def users__none() -> QuerySet[User]:
    return User.objects.none()


def users__all() -> QuerySet[User]:
    return User.objects.all()
