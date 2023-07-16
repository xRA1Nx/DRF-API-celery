from rest_framework import fields
from rest_framework.fields import SerializerMethodField, CharField
from restdoctor.rest_framework.schema import SchemaWrapper
from restdoctor.rest_framework.serializers import ModelSerializer, Serializer

from apps.work_task.logic.facades.work_task import work_task__period
from apps.work_task.models import WorkTask


class WorkTaskDefaultSerializer(ModelSerializer):
    class Meta:
        model = WorkTask
        fields = '__all__'


class WorkTaskDetailSerializer(ModelSerializer):
    class Meta:
        model = WorkTask
        fields = '__all__'

    task_period = SchemaWrapper(
        SerializerMethodField(help_text='Время выполнения задачи'), schema_type=fields.IntegerField()
    )

    def get_task_period(self, obj: WorkTask) -> int:
        return work_task__period(work_task=obj)


class WorkTaskResponseSerializer(Serializer):
    message = CharField(help_text='сообщение об успешном запуске задачи.')