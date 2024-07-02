
import apps.ingredients.domain.ingredient
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import json
import pytest
from apps.ingredients.application.errors.ingredients_not_found import (
    IngredientsNotFoundApplicatonError)


pytestmark = pytest.mark.asyncio

class TestIngredientsRoute:
        
    async def test_get_all_ingredients_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        res = await client.get("/api/v1/ingredient/getall")
        assert res.status_code == 200

    async def test_get_ingredient_by_id_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        try:
            res = await client.get("/api/v1/ingredient/get/3fa85f64-5717-4562-b3fc-2c963f66afa6")
        except Exception as e:
            assert isinstance(e, IngredientsNotFoundApplicatonError)
        
        