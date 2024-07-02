from fastapi import FastAPI
import pytest
from fastapi.testclient import TestClient

# @pytest.fixture
# def new_blog():
#   return BlogCreate(
#   title = "test title",
#   author = "test author",
#   content = "test content",
#   )


@pytest.fixture
def app() -> FastAPI:
    from main import get_application
    return get_application()

@pytest.fixture
def client(app: FastAPI) -> FastAPI:
    client = TestClient(app)
    return client

# @pytest.fixture

# def client(app: FastAPI) -> FastAPI:
#     from dependencies import get_db, override_get_db # <---- agregado nuevo
#     app.dependency_overrides[get_db] = override_get_db 

#     client = TestClient(app)
#     return client

