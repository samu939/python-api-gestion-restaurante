from apps.plates.domain.value_objects.plate_id import PlateId
from core.application.errors.application_errors import ApplicationError

class PlateNotFoundApplicatonError(ApplicationError):
    def __init__(self, plate_id: PlateId):
        super().__init__(f"plato con el id {plate_id.value} no fue encontrado", 404, self.__class__.__name__)