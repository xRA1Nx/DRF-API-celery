from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from restdoctor.rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin, CreateModelMixin
from restdoctor.rest_framework.viewsets import ListModelViewSet

from apps.work_task.api.serializers.work_task import WorkTaskDefaultSerializer, WorkTaskDetailSerializer, \
    WorkTaskResponseSerializer
from apps.work_task.logic.facades.async_facade import async__work_task__start
from apps.work_task.logic.facades.work_task import work_task__create, work_task__check_status_and_start, \
    work_task__check_status_and_finish
from apps.work_task.logic.interactors.work_task import work_task__start, work_task__finish
from apps.work_task.logic.selectors.work_task import work_tasks__all


class WorkTaskViewSet(ListModelViewSet, RetrieveModelMixin, DestroyModelMixin, CreateModelMixin):
    queryset = work_tasks__all()
    filter_backends = (DjangoFilterBackend,)
    schema_tags = ['WorkTask']

    serializer_class_map = {
        'default': WorkTaskDefaultSerializer,
        'retrieve': {
            'response': WorkTaskDetailSerializer
        },
        'create': {
            'response': WorkTaskDetailSerializer
        },
        'start': {
            'response': WorkTaskResponseSerializer
        },
        'finish': {
            'response': WorkTaskResponseSerializer
        }

    }

    def perform_create(self, serializer: WorkTaskDetailSerializer) -> None:
        serializer.instance = work_task__create()

    @action(methods=['post'], detail=True)
    def start(self, request: Request, pk: int) -> Response:
        work_task__check_status_and_start(work_task_pk=pk)
        response_serializer = self.get_response_serializer(
            instance={'message': 'задача запущена'}
        )
        return Response(status=status.HTTP_200_OK, data=response_serializer.data)

    @action(methods=['post'], detail=True)
    def finish(self, request: Request, pk: int) -> Response:
        work_task__check_status_and_finish(work_task_pk=pk)
        response_serializer = self.get_response_serializer(
            instance={'message': 'задача выполнена'}
        )
        return Response(status=status.HTTP_200_OK, data=response_serializer.data)
