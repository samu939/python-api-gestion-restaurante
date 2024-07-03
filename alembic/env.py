import os
import pathlib
import sys

from logging.config import fileConfig
import logging
from typing import Literal

import alembic
from loguru import logger
from psycopg2 import DatabaseError
from sqlalchemy import create_engine, engine_from_config, pool


# we're appending the app directory to our path here so that we can import config easily
# sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from db.db_base import metadata
from config import DATABASE_URL, POSTGRES_DB  # noqa

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = alembic.context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option("sqlalchemy.url", str(DATABASE_URL))

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_online() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    DB_URL = f"{DATABASE_URL}_test_2" if os.environ.get("TESTING") else str(DATABASE_URL)

    # handle testing config for migrations
    if os.environ.get("TESTING"):
        # connect to primary db
        default_engine = create_engine(str(DATABASE_URL), isolation_level="AUTOCOMMIT")
        # drop testing db if it exists and create a fresh one
        with default_engine.connect() as default_conn:
            default_conn.execute(f"DROP DATABASE IF EXISTS {POSTGRES_DB}_test")
            default_conn.execute(f"CREATE DATABASE {POSTGRES_DB}_test")

    connectable = config.attributes.get("connection", None)
    config.set_main_option("sqlalchemy.url", DB_URL)

    if connectable is None:
        connectable = engine_from_config(
            config.get_section(config.config_ini_section),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

    with connectable.connect() as connection:
        alembic.context.configure(connection=connection, target_metadata=None)
        with alembic.context.begin_transaction():
            alembic.context.run_migrations()

    # url = config.get_main_option("sqlalchemy.url")
    # context.configure(
    #     url=url,
    #     target_metadata=target_metadata,
    #     literal_binds=True,
    #     dialect_opts={"paramstyle": "named"},
    # )

    # with context.begin_transaction():
    #     context.run_migrations()


def run_migrations_offline() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    if os.environ.get("TESTING"):
        raise DatabaseError(
            "Running testing migrations offline currently not permitted."
        )

    alembic.context.configure(
        url=str(DATABASE_URL),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with alembic.context.begin_transaction():
        alembic.context.run_migrations()


if alembic.context.is_offline_mode():
    logger.info("Running migrations offline")
    run_migrations_offline()
else:
    logger.info("Running migrations online")
    run_migrations_online()
