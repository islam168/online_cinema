# online_cinema

## Описание проекта
> Онлайн кинотеатр  для просмотра фильмов и сериалов, где пользователи 
> могут купив одну из подписок предоставленых на сайте для просмотра контента.
> Есть 2 вида подписок базовый и премиум (также могут быть и другие). Премиум отличается от базового тем, что
> новый контент доступен для премиум пользователей на 1 день раньше, чем тем 
> кто купил базовый, длительность подписок 30 дней, другие подписки могут длится дольше. 
> Пользователь могут выставлять оценку фильму от 1 до 10 и писать отзывы. Есть возрастной рейтинг,
> если пользователю меньше лет, чем в возрастном рейтинге фильма или сериала, 
> блокируется доступ к просмотру. 

## Какие технологии использованы
- Linux
- PostgreSQL
- Python 3.10
  - Django 4
  - Django Rest Framework

## Как поднять проект локально ?
### Последовательность действий
```.bash
    $ git clone https://github.com/islam168/online_cinema.git
    $ cd online_cinema/
    $ virtualenv venv
    $ pip install -r requirements/local.txt
```
Затем необходимо создать в PostgreSQL создать БД

После создания БД, необходимо применить миграцию, после запуск тестового сервера:
```.bash
    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver
```
