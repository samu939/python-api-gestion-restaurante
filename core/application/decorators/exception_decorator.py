from typing import TypeVar, Generic

from loguru import logger


from ..services.application_service import ApplicationService
from ..results.result_wrapper import Result

T = TypeVar('T')
R = TypeVar('R')

class ExceptionDecorator(ApplicationService[T, R], Generic[T, R]):
    def __init__(self, service: ApplicationService[T, R]):
        self._service = service

    async def execute(self, input: T) -> Result[R]:
            result = await self._service.execute(input)
            if result.is_error():
                logger.info("error in service") 
            return result