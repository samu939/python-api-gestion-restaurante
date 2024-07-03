
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import json
import loguru
import pytest
from apps.order.application.errors.order_not_found import OrderNotFoundApplicatonError
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError



pytestmark = pytest.mark.asyncio

class TestOrderRoutes:
    
    async def test_get_all_orders_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        res = await client.get("/api/v1/orders/getall/2ea9c01c-4c71-4d8c-9dd7-3e6f2e2243e0")
        assert res.status_code == 200
        
    async def test_get_order_by_id_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        try: 
            res = await client.get("/api/v1/orders/get/2ea9c01c-4c71-4d8c-9dd7-3e6f2e2233e0")
        except Exception as e:
            assert isinstance(e, OrderNotFoundApplicatonError)
            
    async def test_create_order_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "plates": [
                {
                "id": "a40f5bc4-398f-446c-a11b-b6d45815840e",
                "quantity": 1
                }
            ]
        }
        res = await client.post("/api/v1/orders/create", json=data)
    
        assert res.status_code == 200
        
    async def test_create_order_route_with_invalid_plate_id(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        data = {
            "plates": [
                {
                "id": "a40f5bc4-398f-446c-a11b-b6d45815841e",
                "quantity": 1
                }
            ]
        }
        try: 
            res = await client.post("/api/v1/orders/create", json=data)
        except Exception as e:
            assert isinstance(e, PlateNotFoundApplicatonError)
    