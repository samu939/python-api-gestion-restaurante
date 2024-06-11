from core.application.errors.application_errors import ApplicationError
from apps.user.domain.value_objects.user_id import UserId

class UserNotFoundApplicatonError(ApplicationError):
    def __init__(self, user_id: UserId):
        super().__init__(f"usuario con el id {user_id.value} no fue encontrado", 404, self.__class__.__name__)