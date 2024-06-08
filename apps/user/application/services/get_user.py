from typing import Awaitable
from apps.user.domain.user import User
from apps.user.domain.repositories.user_repository import UserRepository
from apps.user.domain.value_objects.user_id import UserId
from core.application.services.application_service import ApplicationService
from core.application.results.result_wrapper import Result
from ..errors.user_not_found import UserNotFoundApplicatonError

class GetUserApplicationService(ApplicationService[UserId, User]):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, input: UserId) -> Awaitable[Result[User]]:
        user = await self.user_repository.get_user_by_id(input)
        if user is None:
            return Result[User].failure(
                error=UserNotFoundApplicatonError(input)
            ) # type: ignore
        return Result[User].success(value=user) # type: ignore