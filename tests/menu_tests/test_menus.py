
import apps.ingredients.domain.ingredient
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import json
import pytest
from apps.ingredients.application.errors.ingredients_not_found import (
    IngredientsNotFoundApplicatonError)
from apps.menus.application.errors.menu_not_found import MenuNotFoundApplicatonError
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError


pytestmark = pytest.mark.asyncio

class TestMenusRoute:
        
    async def test_get_all_menus_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        res = await client.get("/api/v1/menus/getall")
        assert res.status_code == 200
    
    async def test_get_menu_by_id_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        try:
            res = await client.get("/api/v1/menus/get/1ccc98db-af71-4127-bbc2-d4e0e4449961")
        except Exception as e:
            assert isinstance(e, MenuNotFoundApplicatonError)