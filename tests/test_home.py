from fastapi import FastAPI, status
from fastapi.testclient import TestClient
import pytest

class TestHomeRoute:
    def test_home_route(self, app: FastAPI, client: TestClient) -> None:
        res = client.get("/")
        assert res.status_code == 200
        assert res.json() == {"message": "Bienvenido al backend del Sistema de Desarrollo de APIs con Python"}