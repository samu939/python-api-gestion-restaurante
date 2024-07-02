from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import pytest

pytestmark = pytest.mark.asyncio

class TestHomeRoute:
    async def test_home_route(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.get("/")
        assert res.status_code == 200
        assert res.json() == {"message": "Bienvenido al backend del Sistema de Desarrollo de APIs con Python"}