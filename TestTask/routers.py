from os import path

from django.urls.conf import path, include
from rest_framework.routers import DefaultRouter

from apps.users.api.viewsets.user import UserViewSet
from apps.work_task.api.viewsets.work_task import WorkTaskViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('work_tasks', WorkTaskViewSet, basename='work_tasks')

urlpatterns = [path('', include(router.urls))]
