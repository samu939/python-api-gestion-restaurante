from uuid import UUID
from databases import Database
from fastapi import APIRouter, Depends

from apps.auth.infraestructure.dependecies.auth_dependecies import get_current_active_user
from apps.menus.application.services.get_all_menus_application_service import GetAllMenusApplicationService
from apps.menus.application.services.get_menu_application_service import GetMenuByIdApplicationService
from apps.menus.domain.value_objects.menu_id import MenuId
from apps.menus.infraestructure.mappers.menus_mapper import MenuMapper
from apps.menus.infraestructure.repositories.db_menus_repository import DbMenusRepository
from apps.menus.infraestructure.responses.menus_responses import GetAllMenusResponse, GetMenuResponse, GetMenuWithPlatesResponse
from apps.plates.infrastructure.mappers.plates_mapper import PlateMapper
from apps.plates.infrastructure.repositories.db_plates_repository import DbPlatesRepository
from apps.user.infrastructure.db_entity.user_in_db import UserInDB
from core.application.decorators.exception_decorator import ExceptionDecorator
from db.db_dependencies import get_database


menus_router = APIRouter(
    prefix="/menus",
    tags=["menu"],
    responses={404: {"description": "Not found"}},
)

@menus_router.get("/getall", response_model=GetAllMenusResponse, name="menu:getAll")
async def getMenus(
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    
    service = ExceptionDecorator(GetAllMenusApplicationService(menus_repository= DbMenusRepository(db, MenuMapper())))
    response = (await service.execute(None)).unwrap()
    menus: list[GetMenuResponse] = []

    for menu in response:
        menus.append({
            'id': menu.id.value,
            'name': menu.name.value
        })
    
    return GetAllMenusResponse(menus=menus)

@menus_router.get("get/{id}", response_model=GetMenuWithPlatesResponse, name="menu:getById")
async def getPlateById(
    id: UUID,
    db: Database = Depends(get_database),
    current_user: UserInDB = Depends(get_current_active_user)
):
    service = ExceptionDecorator(GetMenuByIdApplicationService(menus_repository=DbMenusRepository(db, MenuMapper()), plates_repository=DbPlatesRepository(db, PlateMapper())))
    response = (await service.execute(MenuId(id))).unwrap()
    return response