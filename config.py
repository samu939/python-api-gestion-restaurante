import os
from typing import Optional

from databases import DatabaseURL
from pydantic import PostgresDsn
from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

PROJECT_NAME = "FASTAPI_TDD_DEMO"
DESCRIPTION = "Proyecto Demo Para Desarrollo de APIs con Python"
DEBUG: bool = False
TIMEZONE: str = "UTC"

VERSION = "1.0.0"
API_PREFIX = "/api/v1"

POSTGRES_USER = config("POSTGRES_USER", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=Secret)
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="db")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str)

TEST_DATABASE_URL = config(
    "TEST_DATABASE_URL",
    cast=DatabaseURL,
    default=f"sqlite:///./test.db",
)
# auth and jwt
SECRET_KEY = config("SECRET_KEY", cast=Secret)
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str)
JWT_AUDIENCE = config("JWT_AUDIENCE", cast=str)
JWT_TOKEN_PREFIX = config("JWT_TOKEN_PREFIX", cast=str)
AES_KEY = config("AES_KEY", cast=str)
AES_BLOCKSIZE = config("AES_BLOCKSIZE", cast=int)

DATABASE_URL = config(
    "DATABASE_URL",
    cast=DatabaseURL,
    default=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}",
)


DB_MIN_SIZE: int = 2
DB_MAX_SIZE: int = 15
DB_FORCE_ROLL_BACK: bool = False
