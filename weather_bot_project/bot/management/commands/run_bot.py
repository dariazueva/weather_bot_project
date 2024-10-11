import logging

from django.core.management import BaseCommand

from ...handlers import main

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **options):
        try:
            logger.info("Запуск бота")
            main()
        except Exception as e:
            logger.error(f"Ошибка при запуске бота: {e}")
