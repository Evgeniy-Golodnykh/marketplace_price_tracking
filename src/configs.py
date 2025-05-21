import logging

from constants import (
    DATETIME_FORMAT, DB_DRIVER_NAME, DB_HOST, DB_PORT, LOGFORMAT, POSTGRES_DB,
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
    """Set logging configuration."""

    logging.basicConfig(
        datefmt=DATETIME_FORMAT,
        format=LOGFORMAT,
        level=logging.INFO,
    )
