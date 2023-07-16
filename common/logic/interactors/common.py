import traceback
import typing

from rest_framework.utils import model_meta

from common.common_types import DjangoModel, GenericContext


def create_model_instance(  # noqa: CAC001 because used DRF realisation
    *, model_class: typing.Type[DjangoModel], validated_data: GenericContext
) -> DjangoModel:
    """
    We have a bit of extra checking around this in order to provide
    descriptive messages when something goes wrong, but this method is
    essentially just:

        return ExampleModel.objects.create(**validated_data)

    If there are many to many fields present on the instance then they
    cannot be set until the model is instantiated, in which case the
    implementation is like so:

        example_relationship = validated_data.pop('example_relationship')
        instance = ExampleModel.objects.create(**validated_data)
        instance.example_relationship = example_relationship
        return instance

    The default implementation also does not handle nested relationships.
    If you want to support writable nested relationships you'll need
    to write an explicit `create_model_instance()` method.
    """

    # Remove many-to-many relationships from validated_data.
    # They are not valid arguments to the default `.create()` method,
    # as they require that the instance has already been saved.
    info = model_meta.get_field_info(model_class)
    many_to_many = {}
    for field_name, relation_info in info.relations.items():
        if relation_info.to_many and (field_name in validated_data):
            many_to_many[field_name] = validated_data.pop(field_name)

    try:
        instance = model_class._default_manager.create(**validated_data)
    except TypeError:
        tb = traceback.format_exc()
        msg = (
            'Got a `TypeError` when calling `{model}.{manager}.create()`. '
            'This may be because you have a writable field on the '
            'serializer class that is not a valid argument to '
            '`{model}.{manager}.create()`.\nOriginal exception was:\n {traceback}'.format(
                model=model_class.__name__, manager=model_class._default_manager.name, traceback=tb
            )
        )
        raise TypeError(msg)

    # Save many-to-many relationships after the instance is created.
    if many_to_many:
        for field_name, value in many_to_many.items():
            field = getattr(instance, field_name)
            field.set(value)

    return instance


def update_model_instance(  # noqa: CAC001 because used DRF realisation
    *, instance: DjangoModel, validated_data: GenericContext, update_fields: list[str] | None = None
) -> DjangoModel:
    info = model_meta.get_field_info(instance)

    # Simply set each attribute on the instance, and then save it.
    # Note that unlike `create_model_instance()` we don't need to treat many-to-many
    # relationships as being a special case. During updates we already
    # have an instance pk for the relationships to be associated with.
    m2m_fields = []
    for attr, value in validated_data.items():
        if attr in info.relations and info.relations[attr].to_many:
            m2m_fields.append((attr, value))
        else:
            setattr(instance, attr, value)

    instance.save(update_fields=update_fields)

    # Note that many-to-many fields are set after updating instance.
    # Setting m2m fields triggers signals which could potentially change
    # updated instance and we do not want it to collide with update_model_instance()
    for attr, value in m2m_fields:
        field = getattr(instance, attr)
        field.set(value)

    return instance
