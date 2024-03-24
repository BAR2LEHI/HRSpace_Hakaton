# HRSpace_Hakaton
## Мини-гайд по проекту
1. Установить зависимости из файла **requirements.txt**
2. Создайте в головной директории файл **.env** и впишите в него данные по образцу:
```
POSTGRES_PASSWORD=YOUR_PASSWORD_DB
POSTGRES_USER=USER_NAME_DB
POSTGRES_DB=DB_NAME
POSTGRES_PORT=PORT # Для Postgre стандартный - 5432
POSTGRES_HOST=localhost
```
Так же проверьте что новая база данных уже создана в PostgreSQL

3. В директории **src** размещён файл **database.py**. Он отвечает за подключение к Базе данных и создании сессий для дальнейшей работы с БД.
В файле указаны поясняющие комментарии.


4.В директории **src/our_future_app/** расположен файл с тестовой моделью.
Создать файл миграции можно с помощью команды:
```
alembic revision --autogenerate -m 'Название миграции'
```
И запустить файл командой:
```
alembic upgrade head
```

