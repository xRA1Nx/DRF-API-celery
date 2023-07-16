1) установка зависимостей pip install -r req.txt
2) docker compose up - поднимаем постгрю + redis , в контенер постгри зашит дамп со всеми применеными миграциями
3) celery -A TestTask worker -l info - поднимаем таски
4) celery -A TestTask beat -l info - задачи по расписанию
5) сделан 1 тест как пример test__user__create
6) не использовал шину данных django-chanels ранее не юзал, не хватило времени

