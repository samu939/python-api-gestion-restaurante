from fastapi import APIRouter

from apps.auth.infraestructure.routes.auth_routes import auth_router




router = APIRouter()
router.include_router(auth_router)