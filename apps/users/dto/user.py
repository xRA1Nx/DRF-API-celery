from common.dto.common import BaseDto


class UserCreateRequestDto(BaseDto):
    first_name: str
    last_name: str
    middle_name: str | None
    email: str
