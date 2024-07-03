from databases import Database
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.dto.login_response import AuthResponse
from apps.auth.application.services.login_service import loginService
from apps.auth.application.services.register_service import registerService
from apps.auth.infraestructure.jwt.jwt_generator import jwtGenerator
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from apps.user.infrastructure.mappers.user_mapper import UserMapper
from apps.user.infrastructure.register_entry import RegisterUserEntry
from apps.user.infrastructure.repositories.db_user_repository import dbUserRepository
from core.application.decorators.exception_decorator import ExceptionDecorator
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
    result = await ExceptionDecorator(loginService(db,dbUserRepository(db, user_mapper= UserMapper()), jwtGenerator())).execute(
        loginDto(username=form_data.username, password=form_data.password)
    )

    return result.unwrap()

@auth_router.post("/register", response_model=AuthResponse, name="auth:register")
async def register(
    form_data: RegisterUserEntry,
    db: Database = Depends(get_database),
):
    result = await ExceptionDecorator(registerService(db,dbUserRepository(db, user_mapper= UserMapper()), jwtGenerator())).execute(form_data)

    return result.unwrap()