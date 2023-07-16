from django_filters.rest_framework import DjangoFilterBackend
from restdoctor.rest_framework.viewsets import ModelViewSet

from apps.users.api.serializers.user import UserDefaultSerializer, UserCreateSerializer
from apps.users.dto.user import UserCreateRequestDto
from apps.users.logic.facades.user import user__create
from apps.users.logic.selectors.user import users__all


class UserViewSet(ModelViewSet):
    queryset = users__all().order_by('-id')
    filter_backends = (DjangoFilterBackend,)
    schema_tags = ['Users']

    serializer_class_map = {
        'default': UserDefaultSerializer,
        'create': {
            'request': UserCreateSerializer,
            'response': UserDefaultSerializer,
        }
    }

    def perform_create(self, serializer: UserCreateSerializer) -> None:
        create_request_dto = UserCreateRequestDto(**serializer.validated_data)
        serializer.instance = user__create(
            dto=create_request_dto
        )
