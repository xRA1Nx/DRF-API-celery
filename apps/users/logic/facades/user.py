from apps.users.dto.user import UserCreateRequestDto
from apps.users.models import User
from common.logic.interactors.common import create_model_instance


def user__create(*, dto: UserCreateRequestDto):
    dto_dict = dto.dict(exclude_unset=True)
    dto_dict['login'] = dto.email

    return create_model_instance(
        model_class=User,
        validated_data=dto_dict
    )
