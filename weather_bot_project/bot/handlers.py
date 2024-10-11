import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from .models import Log

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "Привет! Я бот для получения информации о погоде.\n"
        "Используй команду /weather <город> для получения текущей погоды.\n"
        "Этот бот создан в качестве теста для компании BobrAi."
    )
    await update.message.reply_text(welcome_message)


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    command = update.message.text
    args = context.args

    if not args:
        error_message = "Пожалуйста, укажи город после команды /weather.\nПример: /weather Москва"
        await update.message.reply_text(error_message)
        Log.objects.create(
            user_id=user_id,
            command=command,
            response=error_message
        )
        return

    city = ' '.join(args)
    weather_data = get_weather(city)

    if 'error' in weather_data:
        response = weather_data['error']
    else:
        response = (
            f"Погода в {city}:\n"
            f"Температура: {weather_data['temperature']}°C\n"
            f"Ощущается как: {weather_data['feels_like']}°C\n"
            f"Описание: {weather_data['description']}\n"
            f"Влажность: {weather_data['humidity']}%\n"
            f"Скорость ветра: {weather_data['wind_speed']} м/с"
        )

    await update.message.reply_text(response)

    Log.objects.create(
        user_id=user_id,
        command=command,
        response=response
    )


def get_weather(city):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    )
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('cod') != 200:
            return {'error': data.get('message', 'Не удалось получить данные о погоде.')}

        weather_info = {
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }
        return weather_info

    except Exception as e:
        logger.error(f"Ошибка при получении погоды: {e}")
        return {'error': 'Произошла ошибка при получении данных о погоде.'}


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))

    app.run_polling()
