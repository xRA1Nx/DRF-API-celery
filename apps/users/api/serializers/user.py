from rest_framework import fields
from rest_framework.fields import SerializerMethodField
from restdoctor.rest_framework.schema import SchemaWrapper
from restdoctor.rest_framework.serializers import ModelSerializer

from apps.users.models import User
from common.constant.common import MAIN_READ_ONLY_FIELDS
from common.logic.facades.names import physical__entity_full_name


class UserDefaultSerializer(ModelSerializer):
    """
    Сериализация пользовател(я)/ей
    """

    class Meta:
        model = User
        exclude = ('uuid', 'user_permissions', 'groups')

        read_only_fields = MAIN_READ_ONLY_FIELDS

        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    full_name = SchemaWrapper(
        SerializerMethodField(help_text='full_name string'), schema_type=fields.CharField()
    )

    def get_full_name(self, obj: User) -> str:
        return physical__entity_full_name(instance=obj)


class UserCreateSerializer(ModelSerializer):
    """
    Сериализация пользовател(я)/ей
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'middle_name', 'email')
