from factory import Sequence
from factory.django import DjangoModelFactory
from faker import Faker

from apps.users.models import User

fake = Faker()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    login = Sequence(lambda n: f'user{n}')
    first_name = fake.first_name()
    last_name = fake.last_name()
    is_staff = False
    is_superuser = False
    email = fake.email()
