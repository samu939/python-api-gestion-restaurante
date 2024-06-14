from fastapi import APIRouter

from apps.auth.infraestructure.routes.auth_routes import auth_router
from apps.ingredients.infrastructure.routes.ingredients_routes import ingredient_router
from apps.store.infrastructure.routes.store_routes import store_router
from apps.user.infrastructure.routes.user_routes import user_router




router = APIRouter()
router.include_router(auth_router)
router.include_router(user_router)
router.include_router(ingredient_router)
router.include_router(store_router)