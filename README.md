# HRSpace

## Авторы проекта

- [Vladislav Tarasov](https://github.com/BAR2LEHI)
- [Dmitriy Pokrovskiy](https://github.com/mityay36)
- [Nikita Prokofev](https://github.com/lordrie)

## Содержание
- [Авторы проекта](#авторы-проекта)
- [Технологии](#технологии)
- [Описание](#Описание)
- [Запуск проекта](#запуск-проекта)
- [Тестирование](#тестирование)

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

## Описание:
Добавьте краткое описание проекта, опишите какую задачу он решает. 1-3 предложения будет достаточно. Добавьте бейджи для важных статусов проекта: статус разработки (в разработке, на поддержке и т.д.), статус билда, процент покрытия тестами и тд.


## Запуск проекта

### Для запуска проекта локально (доступ по http://127.0.0.1:8000/)

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
uvicorn src.main:app --uvicorn
```

### Для запуска контейнеров (доступ по http://localhost:8000/)
- Перейти в папку и создать в нём .env файл согласно примеру:
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
### Для запуска проекта на сервере (доступ по http://(domen_name)/)

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

## Запуск тестов
- Для запуска тестов необходимо выполнить команду:
```
python tests.py
```
## К проекту подключена документация, в которой можно ознакомиться с эндпоинтами и методами, а также с примерами запросов, ответов и кода:
```
http://127.0.0.1:8000/api/docs/
http://127.0.0.1:8000/api/redoc/
```