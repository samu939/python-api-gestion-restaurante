import os
import warnings
import alembic
from asgi_lifespan import LifespanManager
from databases import Database
from fastapi import FastAPI
from httpx import AsyncClient
import pytest
from fastapi.testclient import TestClient
from alembic.config import Config
import pytest_asyncio

from apps.auth.infraestructure.service.auth_services import AuthService
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from apps.user.infrastructure.repositories.db_user_repository import dbUserRepository
from config import JWT_TOKEN_PREFIX, SECRET_KEY
from apps.user.infrastructure.mappers.user_mapper import UserMapper

# Aplicar migraciones al comienzo y fin de la sesión de pruebas
@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore")
    os.environ["TESTING"] = "1"
    config = Config("alembic.ini")

    alembic.command.upgrade(config, "head")
    yield
    alembic.command.downgrade(config, "base")


# Se crea una nueva aplicación para pruebas
@pytest.fixture
def app(apply_migrations: None) -> FastAPI:
    from main import get_application
    return get_application()


# Se obtiene una referencia a la base de datos cuando se haga necesario
@pytest.fixture
def db(app: FastAPI) -> Database:
    return app.state._db


@pytest_asyncio.fixture
async def client(app: FastAPI) -> AsyncClient: #type: ignore
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"},
        ) as client:
            yield client


@pytest.fixture
async def authorized_client(client: AsyncClient, db: Database) -> AsyncClient:

    user_repo = dbUserRepository(db, user_mapper=UserMapper())
    user_test = await user_repo.get_user_by_username("admin")

    access_token = AuthService().create_access_token_for_user(
        user=user_test, secret_key=str(SECRET_KEY)
    )

    client.headers = {
        **client.headers,
        "Authorization": f"{JWT_TOKEN_PREFIX} {access_token}",
    }

    return client


# @pytest.fixture

# def client(app: FastAPI) -> FastAPI:
#     from dependencies import get_db, override_get_db # <---- agregado nuevo
#     app.dependency_overrides[get_db] = override_get_db 

#     client = TestClient(app)
#     return client

