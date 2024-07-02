
from fastapi import FastAPI, status
from fastapi.testclient import TestClient
from httpx import AsyncClient
import json
import loguru
import pytest

from apps.store.domain.exceptions.inventory_name_not_valid_exception import InventoryNameNotValid


pytestmark = pytest.mark.asyncio

class TestStoreRoute:
    
    async def test_get_all_stores_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        res = await client.get("/api/v1/store/getall")
        assert res.status_code == 200
    
    async def test_create_store_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        store = {
            "name": "Store 1"
            }
        res = await client.post("/api/v1/store/create", json=store)
        assert res.status_code == 200
        
    async def test_invalid_create_store_route(self, app: FastAPI, authorized_client: AsyncClient) -> None:
        client = await authorized_client
        store = {
            "name": ""
            }
        try:
            res = await client.post("/api/v1/store/create", json=store)
        except Exception as e:
            assert isinstance(e, InventoryNameNotValid)
