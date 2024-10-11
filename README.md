# Weather Bot Project

## Описание

Telegram-бот для получения информации о погоде в указанном городе. Бот был создан в качестве тестового задания для компании BobrAi. В качестве API для получения информации о погоде выступал OpenWeatherMap.

## Требования

- Python 3.8+
- PostgreSQL

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:dariazueva/weather_bot_project.git
```

```
cd weather_bot_project 
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Создайте файл .env и заполните его своими данными по образцу:

```
WEATHER_API_KEY = ваш-токен-OpenWeatherMap
TELEGRAM_TOKEN = ваш-токен-телеграм-бота
DATABASE_NAME=weather_bot_db
DATABASE_USER=adrea
DATABASE_PASSWORD=secret
DATABASE_HOST=localhost
DATABASE_PORT=5431
```

В консоли пропишите команду для запуска контейнера базы данныхЖ
```
docker run --name weather_bot_db --env-file .env -p 5431:5432 postgres:13.10
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить бот:
```
python manage.py run_bot
```

Запустить апишку:

```
python manage.py runserver
```

Запустите тесты с помощью команды:
```
python manage.py test
```

## Автор
Зуева Дарья Дмитриевна
Github https://github.com/dariazueva/