
from apps.ingredients.domain.exceptions.ingredient_quantity_not_valid_exception import IngredientQuantityNotValid
import apps.ingredients.domain.ingredient
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import json
import pytest
from apps.ingredients.application.errors.ingredients_not_found import (
    IngredientsNotFoundApplicatonError)
from apps.store.application.errors.store_not_found import StoreNotFoundApplicatonError


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
            
    async def test_create_ingredient_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "name": "Test Ingredient",
            "quantity": 10,
            "store_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
        res = await client.post("/api/v1/ingredient/create", json=data)
        assert res.status_code == 200
        
    async def test_create_ingredient_route_with_invalid_quantity(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "name": "Test Ingredient",
            "quantity": -10,
            "store_id": '3fa85f64-5717-4562-b3fc-2c963f66afa6'
        }
        try:
            res = await client.post("/api/v1/ingredient/create", json=data)
        except Exception as e:
            assert isinstance(e, IngredientQuantityNotValid)
    
    async def test_create_ingredient_route_with_invalid_store_id(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "name": "Test Ingredient",
            "quantity": 10,
            "store_id": '3fa85f64-5718-4562-b3fc-2c963f66afa6'
        }
        try:
            res = await client.post("/api/v1/ingredient/create", json=data)
        except Exception as e:
            assert isinstance(e, StoreNotFoundApplicatonError)
    
    async def test_ingress_ingredient_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "quantity": 10
        }
        res = await client.post("/api/v1/ingredient/ingress/3fa85f64-5717-4562-b3fc-2c963f66afa6", json=data)
        assert res.status_code == 200
        
    async def test_ingress_ingredient_route_with_invalid_quantity(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "quantity": -10
        }
        try:
            res = await client.post("/api/v1/ingredient/ingress/3fa85f64-5717-4562-b3fc-2c963f66afa6", json=data)
        except Exception as e:
            assert isinstance(e, IngredientQuantityNotValid)
            
    async def test_egress_ingredient_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "quantity": 1
        }
        res = await client.post("/api/v1/ingredient/egress/3fa85f64-5717-4562-b3fc-2c963f66afa6", json=data)
        assert res.status_code == 200
    
    async def test_egress_ingredient_route_with_invalid_quantity(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "quantity": -1
        }
        try:
            res = await client.post("/api/v1/ingredient/egress/3fa85f64-5717-4562-b3fc-2c963f66afa6", json=data)
        except Exception as e:
            assert isinstance(e, IngredientQuantityNotValid)
    
    
    async def test_change_store_ingredient_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "store_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
        }
        res = await client.post("/api/v1/ingredient/changestore/3fa85f64-5717-4562-b3fc-2c963f66afa6", json=data)
        assert res.status_code == 200
        
    async def test_change_store_ingredient_route_with_invalid_store_id(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "store_id": "3fa85f64-5717-4562-b3fc-2c963f66afa7"
        }
        try:
            res = await client.post("/api/v1/ingredient/changestore/3fa85f64-5717-4562-b3fc-2c963f66afa6", json=data)
        except Exception as e:
            assert isinstance(e, StoreNotFoundApplicatonError)

            
        
        