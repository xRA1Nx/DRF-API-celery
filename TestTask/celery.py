import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestTask.settings')

app = Celery('TestTask')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday': {
        'task': 'apps.work_task.tasks.finished_work_task__db_cleaner__task',
        'schedule': 10,
        # 'schedule': crontab(hour='10', minute='0', day_of_week='monday'),
        'args': (),
    },
}
