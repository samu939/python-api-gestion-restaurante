from apps.menus.domain.value_objects.menu_id import MenuId
from core.application.errors.application_errors import ApplicationError

class MenuNotFoundApplicatonError(ApplicationError):
    def __init__(self, menu_id: MenuId):
        super().__init__(f"Menú con el id {menu_id.value} no fue encontrado", 404, self.__class__.__name__)