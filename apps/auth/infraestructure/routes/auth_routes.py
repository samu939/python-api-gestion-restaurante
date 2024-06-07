from typing import List
from uuid import UUID

from databases import Database
from fastapi import APIRouter, Body, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from icecream import ic
from loguru import logger
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.services.login_service import loginService
from apps.auth.infraestructure.entities.token import (
    AuthResponse,
)

from apps.auth.infraestructure.jwt.jwt_generator import jwtGenerator
from apps.user.infrastructure.repositories.db_user_repository import dbUserRepository
from db.db_dependencies import get_database

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

@auth_router.post("/login", response_model=AuthResponse, name="auth:login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
    db: Database = Depends(get_database),
):
    result = await loginService(db,dbUserRepository(db), jwtGenerator()).execute(
        loginDto(username=form_data.username, password=form_data.password)
    )

    return result.unwrap()
