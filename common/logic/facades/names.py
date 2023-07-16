from common.logic.interactors.names import field__check_for_str_and_strip
from common.models.main_abstract import AbstractMainModel


def physical__entity_full_name(*, instance: AbstractMainModel) -> str:
    """
    Возвращает полное имя сущности

    Важно: Во избежание возможных проблем с преобразованием поля в строку
    и применения к нему строковых методов все поля 'завернуты'
    во вспомогательную функцию field__check_for_str_and_strip
    """
    last_name = field__check_for_str_and_strip(field_name='last_name', instance=instance)
    first_name = field__check_for_str_and_strip(field_name='first_name', instance=instance)
    middle_name = field__check_for_str_and_strip(field_name='middle_name', instance=instance)

    return f'{last_name} {first_name} {middle_name}'.rstrip().title()
