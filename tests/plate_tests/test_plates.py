
import apps.ingredients.domain.ingredient
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import json
import pytest
from apps.ingredients.application.errors.ingredients_not_found import (
    IngredientsNotFoundApplicatonError)
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError


pytestmark = pytest.mark.asyncio

class TestPlatesRoute:
        
    async def test_get_all_plates_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        res = await client.get("/api/v1/plates/getall")
        assert res.status_code == 200

    async def test_get_plate_by_id_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        try:
            res = await client.get("/api/v1/plates/get/a40f5bc4-398f-446c-a11b-b6d45815840e")
        except Exception as e:
            assert isinstance(e, PlateNotFoundApplicatonError)
        
    async def test_create_plate_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        plate = {
            "name": "Plate 1",
            "description": "Description 1",
            "price": 10.0,
            "ingredients": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "quantity": 1
                }
            ]}
        res = await client.post("/api/v1/plates/create", json=plate)
        assert res.status_code == 200

    async def test_create_plate_route_with_invalid_ingredient(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        plate = {
            "name": "Plate 1",
            "description": "Description 1",
            "price": 10.0,
            "ingredients": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "quantity": 1
                },
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa7",
                    "quantity": 1
                }
            ]
            }
        try:
            res = await client.post("/api/v1/plates/create", json=plate)
        except Exception as e:
            assert isinstance(e, IngredientsNotFoundApplicatonError)
        