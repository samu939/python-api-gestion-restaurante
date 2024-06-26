from typing import List
from databases import Database
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from apps.auth.application.exceptions.auth_exceptions import AuthExceptions
from apps.auth.infraestructure.service.auth_services import AuthService
from apps.user.infrastructure.db_entity.user_in_db import UserInDB, roleEnum
from apps.user.infrastructure.mappers.user_mapper import UserMapper
from apps.user.infrastructure.repositories.db_user_repository import dbUserRepository
from config import API_PREFIX, SECRET_KEY
from db.db_dependencies import get_database



oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{API_PREFIX}/auth/login/")


async def get_user_from_token(
    *, token: str = Depends(oauth2_scheme), db: Database = Depends(get_database)
) -> UserInDB | None:
    user_repo = dbUserRepository(db, UserMapper())
    user = None
    try:
        username = AuthService().get_username_from_token(
            token=token, secret_key=str(SECRET_KEY)
        )
        user = await user_repo.get_user_by_username(username=username)
    except Exception as e:
        raise e

    return user


def get_current_active_user(
    current_user: UserInDB = Depends(get_user_from_token),
) -> UserInDB | None:
    if not current_user:
        raise AuthExceptions.AuthUnauthorizedException()

    return current_user

def role_required(allowed_roles: List[roleEnum]):
    def role_verifier(current_user: UserInDB = Depends(get_current_active_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"User role '{current_user.role.name}' does not have access"
            )
        return current_user
    return role_verifier