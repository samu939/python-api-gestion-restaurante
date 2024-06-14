from apps.store.domain.value_objects.store_id import StoreId
from core.application.errors.application_errors import ApplicationError

class StoreNotFoundApplicatonError(ApplicationError):
    def __init__(self, store_id: StoreId):
        super().__init__(f"Almacen con el id {store_id.value} no fue encontrado", 404, self.__class__.__name__)