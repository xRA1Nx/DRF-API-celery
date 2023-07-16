Портал игровых новостей сделан на основе новостного сайта с тематикой игр blizzard - glasscannon.ru<br>

<b>stack</b>:<br>
  Django, DRF, Docker-compose, PostgreSql, Celery, Redis, DRF, CSS, HTML, JS
 
<b>Конфигурация проекта:</b><br>
  Все личные данные от почты, Редис, берутся из виртуального окружения. Для полного функционирования проекта необходимо указать свои данные либо в settings.py, либо также вынести в .env<br>


<b>Запуск проекта с помощью docker-compose</b><br>

2)docker compose up (пред запуск проекта)<br>
<u>в отдельной консоли:</u><br>
3)docker exec -i db_pg pg_restore -U postgres --verbose --clean --no-acl --no-owner -h localhost -d cism db.sql<br> (установка дампа начальной БД).<br>
4)docker compose down - останавливаем контенеры (для применения изменений в БД)<br>
5)docker compose up - все последующие запуски проекта<br>

Для запуска задач по расписанию:<br>
  2)docker compose run web celery -A TestTask worker -l info -P eventlet  (2-м окном терминала)<br>
  3)docker compose run web celery -A gamenews_proj beat (3м окном терминала)<br>

