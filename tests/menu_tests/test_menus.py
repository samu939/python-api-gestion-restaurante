
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
        res = await client.get("/api/v1/menus/get/1ccc98db-af71-4127-bbc2-d4e0e4449961")
        assert res.status_code == 200
    
    async def test_get_invalid_menu_by_id_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:   
        client = await authorized_client
        try:
            res = await client.get("/api/v1/menus/get/1ccc98db-af71-4127-bbc2-d4e0e4449962")
        except Exception as e:
            assert isinstance(e, MenuNotFoundApplicatonError)
        
    async def test_create_menu_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        menu = {
            "name": "CreateMenu test",
            "plates": ["a40f5bc4-398f-446c-a11b-b6d45815840e"]
            }
        res = await client.post("/api/v1/menus/create", json=menu)
        assert res.status_code == 200

    async def test_create_menu_with_invalid_plate(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        menu = {
            "name": "Menu 1",
            "plates": ["a40f6bc4-398f-446c-a11b-b6d45815840e", "3fa96f64-5717-4562-b3fc-2c963f66afa6"]
            }
        try:
            res = await client.post("/api/v1/menus/create", json=menu)
        except Exception as e:
            assert isinstance(e, PlateNotFoundApplicatonError)
    
    async def test_modify_menu_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        menu = {
            "name": "ModifyMenu 1",
            "plates": ["a40f5bc4-398f-446c-a11b-b6d45815840e"]
            }
        res = await client.put("/api/v1/menus/modify/1ccc98db-af71-4127-bbc2-d4e0e4449961", json=menu)
        assert res.status_code == 200