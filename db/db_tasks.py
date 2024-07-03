import os

from databases import Database
from fastapi import FastAPI
from loguru import logger

from config import (
    DATABASE_URL,
    DB_MIN_SIZE,
    DB_MAX_SIZE
)


async def connect_to_db(app: FastAPI) -> None:
    try:
        DB_URL = f"{DATABASE_URL}_test_2" if os.environ.get("TESTING") else DATABASE_URL
        database = Database(DB_URL, min_size=DB_MIN_SIZE, max_size=DB_MAX_SIZE)
        logger.info(f"Database connection - starting {DATABASE_URL}")
        await database.connect()
        app.state._db = database


        logger.info("Database connection - successful")
    except Exception as e:
        logger.warning("--- DB CONNECTION ERROR ---")
        logger.warning(e)
        logger.warning("--- DB CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()  # database.disconnect()
        logger.info("Database connection - closed")
    except Exception as e:
        logger.warning("--- DB DISCONNECT ERROR ---")
        logger.warning(e)
        logger.warning("--- DB DISCONNECT ERROR ---")

