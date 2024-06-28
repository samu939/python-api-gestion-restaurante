
from typing import Awaitable
from apps.plates.application.errors.plate_not_found import PlateNotFoundApplicatonError
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from apps.plates.domain.value_objects.plate_id import PlateId
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class GetPlateByIdApplicationService(ApplicationService[None, Plate]):
    def __init__(self, plates_repository: PlateRepository) -> None:
        self.plates_repository = plates_repository

    async def execute(self, input: PlateId) -> Awaitable[Result[Plate]]:
        plate = await self.plates_repository.get_plate_by_id(input)
        if plate is None:
            return Result[Plate].failure(
                error=PlateNotFoundApplicatonError(input)
            )
        return Result[Plate].success(value=plate)