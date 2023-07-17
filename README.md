Использована библиотека restdoc, проект оформлен на основании арх гайда BestDoctor , с соответсвующими инструментами (та среда в которой я на данный момент фактически работаю)

1) установка зависимостей pip install -r req.txt
2) docker compose up - поднимаем постгрю + redis
3) python manage.py migrate
4) celery -A TestTask worker -l info - поднимаем таски
5) celery -A TestTask beat -l info - задачи по расписанию



