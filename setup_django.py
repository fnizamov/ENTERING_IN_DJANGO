"""
django-admin startproject <project_name> . - создание проекта 

в папке <project_name> в файле settings нужно настроить связь с базой данных (переменная DATABASE)

указать 'rest_framework' в списке INSTALLED_APPS

python3 manage.py runserver [port_number] - запуск сервера

Миграция - код, который содержит информацию о том, как будут выглядеть таблицы в БД.
    python3 manage.py makemigration - создание миграций
    python3 manage.py migrate - применение миграций (импорт шаблонных таблиц)


python3 manage.py createsuperuser - создание администраторской учетной записи (суперпользователя)

python3 manage.py startapp - создание приложения
"""