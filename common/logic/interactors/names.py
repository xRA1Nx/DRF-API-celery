from common.models.main_abstract import AbstractMainModel


def field__check_for_str_and_strip(*, field_name: str, instance: AbstractMainModel) -> str:
    """
    Проверяет, является ли поле сущности текстовым, и если да, то убирает из него пробелы
    в противном случае возвращает пустую строку
    """
    instance_field = getattr(instance, field_name, '')
    if isinstance(instance_field, str):
        return instance_field.strip()
    return ''
