# FirstDjango_04_02_2026

## инструкция по развертыванию проекта

1. Создать виртуальное окружение

python3 -m venv django_venv

2. активирувать виртуалку

source django_venv/bin/activate

3. установка библиотек

pip install -r requirements.txt

4. Применить миграции
python manage.py migrate

5. запуск сервера

python manage.py runserver

##Запуск 'ipython' в контексте джанго приложений

python manage.py shell_plus --ipython

##Выгрузка и загрузка данных при работе с БД
### Выгрузка данных из БД

python manage.py dumpdata MainApp --indent 4 > MainApp/fixtures/all_items.json


###Загрузка данных

python manage.py loaddata MainApp MainApp/fixtures/all_items.json

##Доп

Расширение шаблонов: Django

ext install batisteo.vccode-django

Добавить в settings.json
    "emmet.includeLanguages": {"django-html": "html"},
    "files.associations": {"*.html":"django-html"}