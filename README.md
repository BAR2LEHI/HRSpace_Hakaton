# HRSpace - [hrspace.sytes.net](https://hrspace.sytes.net)

HRspace - это маркетплейс для подбора сотрудников с помощью частных рекрутеров и кадровых агентств. В рамках данного проекта мы разрабатываем новый билдер заявок, который упрощает процесс подбора для работодателей.

## Авторы проекта

- [Vladislav Tarasov](https://github.com/BAR2LEHI)
- [Dmitriy Pokrovskiy](https://github.com/mityay36)
- [Nikita Prokofev](https://github.com/lordrie)

## Содержание
- [Авторы проекта](#авторы-проекта)
- [Технологии](#технологии)
- [Реализация](#Реализация)
- [Запуск проекта](#запуск-проекта)
- [Запуск тестов](#запуск-тестов)

## Технологии
- Python 3.10
- FastApi 0.110.0
- Uvicorn 0.28.0
- SqlAlchemy 2.0.28
- Alembic 1.13.1
- Redis 4.6.0

- PostgreSQL 13
- Docker
- Nginx

## Реализация:

Проект реализован на **FastAPI**, современном и быстром фреймворке, который использует асинхронный код.
Мы разработали удобную админ-панель на **SqlAdmin**, которая позволяет легко управлять данными.
Использовали Redis в качестве хранилища данных в памяти и кеша, что обеспечивает быстрый доступ к данным.
**Docker** используется для упаковки приложения в контейнеры, что обеспечивает удобство при развёртывании проекта.
**Nginx** используется в качестве веб-сервера, обратного прокси-сервера, что обеспечивает стабильность и производительность веб-приложений.
Так же покрыли тестами **Pytest** главную часть проекта.
Все эти технологии вместе обеспечивают надежность, производительность и гибкость нашего проекта.

## Запуск проекта

### Для запуска локально:

- Клонировать репозиторий и перейти в него:
```
git clone git@github.com:BAR2LEHI/HRSpace_Hakaton.git
cd HRSpace_Hakaton

```
- Создать файл .env в корневой директории и прописать в него свои данные.(Пример env.example)

- Подготовить сервер PostgreSQL согласно данным в вашем .env-файле.

- Cоздать и активировать виртуальное окружение:
```
python -m venv venv
source venv/Scripts/activate
```
- Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
- Создать и применить миграции:
```
alembic revision --autogenerate -m "migration"
alembic upgrade head
```
- Запустить проект:
```
uvicorn src.main:app --reload
```

### Запуск Docker:
- Перейти в папку infra/ и создать в нём .env файл согласно примеру:
```
cd infra/
```
- Запустить сборку  проекта:
```
docker-compose up --build
```
- Создать и применить миграции:
```
docker exec -i backend_app alembic revision --autogenerate -m "MIGRATE"
docker exec -i backend_app alembic upgrade head
```
### Деплой:

- Скопировать на сервер файл docker-compose.prod.yml и рядом с ним создать .env файл (по примеру выше) и nginx.conf с настройками по примеру nginx.conf в папке infra.

- Запустить сборку  проекта:
```
sudo docker compose -f docker-compose.prod.yml up -d
```
- Создать и применить миграции:
```
sudo docker exec -i backend_app alembic revision --autogenerate -m "MIGRATE"
sudo docker exec -i backend_app alembic upgrade head
```

## Запуск тестов:
- Для запуска тестов необходимо зайти в дерикторию выполнить команду:
```
cd tests/
pytest
```
### К проекту подключена документация, а так же админ панель:
```
http://127.0.0.1:8000/api/docs/
http://127.0.0.1:8000/api/redoc/
http://127.0.0.1:8000/api/admin/
```
