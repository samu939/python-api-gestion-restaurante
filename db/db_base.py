import os

from databases import Database
from loguru import logger
import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


def get_db() -> Database:
    database_url = str(config.DATABASE_URL)
    options = {
        "min_size": config.DB_MIN_SIZE,
        "max_size": config.DB_MAX_SIZE,
        "force_rollback": config.DB_FORCE_ROLL_BACK,
    }

    return Database(database_url, **options)


database = get_db()
Base = declarative_base()
metadata = Base.metadata
engine = create_engine(str(config.DATABASE_URL))
