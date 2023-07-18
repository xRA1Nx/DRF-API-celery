import pytest

from apps.users.dto.user import UserCreateRequestDto
from apps.users.logic.facades.user import user__create
from apps.users.models import User


@pytest.mark.django_db()
def test__user__create(mocked__create_model_instance):
    dto_dict = {
        'first_name': 'first_name',
        'last_name': 'last_name',
        'middle_name': 'middle_name',
        'email': 'email@email.email',
    }
    dto = UserCreateRequestDto(**dto_dict)
    dto_dict['login'] = dto.email

    user__create(dto=dto)

    mocked__create_model_instance.assert_called_once_with(
        model_class=User,
        validated_data=dto_dict
    )
