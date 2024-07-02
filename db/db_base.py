import os

from databases import Database
from loguru import logger
import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from alembic import op
from sqlalchemy.engine.reflection import Inspector


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

def table_exists(table_name: str) -> bool:
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    return table_name in tables