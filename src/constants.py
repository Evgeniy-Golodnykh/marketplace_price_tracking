import os

from dotenv import load_dotenv

load_dotenv()

DB_DRIVER_NAME = os.getenv('DB_DRIVER_NAME')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
LOG_FORMAT = '%(asctime)s [%(levelname)s] in %(name)s: %(message)s'

MARKETPLACE_URLS = (
    'https://ozon.ru',
    'https://www.ozon.ru',
    'https://market.yandex.ru',
    'https://www.market.yandex.ru',
    'https://wildberries.ru',
    'https://www.wildberries.ru',
    'https://lamoda.ru'
    'https://www.lamoda.ru'
)
