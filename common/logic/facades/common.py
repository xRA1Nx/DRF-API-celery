import typing

from common.common_types import DjangoModel, GenericContext
from common.logic.interactors.common import (
    create_model_instance as create_model_instance_interactor,
)
from common.logic.interactors.common import (
    update_model_instance as update_model_instance_interactor,
)


def create_model_instance(
    model_class: typing.Type[DjangoModel], validated_data: GenericContext, refresh: bool = False
) -> DjangoModel:
    instance = create_model_instance_interactor(
        model_class=model_class, validated_data=validated_data
    )

    if refresh:
        instance.refresh_from_db()

    return instance


def update_model_instance(
    instance: DjangoModel,
    validated_data: GenericContext,
    refresh: bool = False,
    update_fields: list[str] | None = None,
) -> DjangoModel:
    instance = update_model_instance_interactor(
        instance=instance, validated_data=validated_data, update_fields=update_fields
    )
    if refresh:
        instance.refresh_from_db()

    return instance
