
from typing import Awaitable
from apps.plates.domain.plate import Plate
from apps.plates.domain.repositories.plates_repository import PlateRepository
from core.application.results.result_wrapper import Result
from core.application.services.application_service import ApplicationService


class GetAllPlatesApplicationService(ApplicationService[None, list[Plate]]):
    def __init__(self, plates_repository: PlateRepository) -> None:
        self.plates_repository = plates_repository

    async def execute(self, input: None) -> Awaitable[Result[list[Plate]]]:
        plates = await self.plates_repository.get_all_plates()
        return Result[list[Plate]].success(value=plates)