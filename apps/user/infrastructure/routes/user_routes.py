from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from apps.auth.application.dto.login_dto import loginDto
from apps.auth.application.services.login_service import loginService
from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user
from apps.auth.infraestructure.entities.token import (
    AuthResponse,
)

from apps.auth.infraestructure.jwt.jwt_generator import jwtGenerator
from apps.user.application.services.get_user import GetUserApplicationService
from apps.user.domain.user import User
from apps.user.domain.value_objects.user_id import UserId
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from apps.user.infrastructure.mappers.user_mapper import UserMapper
from apps.user.infrastructure.repositories.db_user_repository import dbUserRepository
from apps.user.infrastructure.responses.user_responses import GetUserResponse
from db.db_dependencies import get_database

user_router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)

@user_router.post("/get", response_model=GetUserResponse, name="user:getById")
async def getUserById(
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user),
):

    return current_user
