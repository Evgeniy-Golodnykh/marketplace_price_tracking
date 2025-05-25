import logging

from core.constants import (
    DATETIME_FORMAT, DB_DRIVER_NAME, DB_HOST, DB_PORT, LOG_FORMAT, POSTGRES_DB,
    POSTGRES_PASSWORD, POSTGRES_USER,
)

DATABASE = {
    'drivername': DB_DRIVER_NAME,
    'host': DB_HOST,
    'port': DB_PORT,
    'username': POSTGRES_USER,
    'password': POSTGRES_PASSWORD,
    'database': POSTGRES_DB,
}


def configure_logging():
    """Set logging configuration for async-friendly app."""

    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
    )

    logging.getLogger('asyncio').setLevel(logging.WARNING)
    logging.getLogger('aiogram.event').setLevel(logging.WARNING)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
