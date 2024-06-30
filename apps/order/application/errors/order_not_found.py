from core.application.errors.application_errors import ApplicationError

class OrderNotFoundApplicatonError(ApplicationError):
    def __init__(self, order_id: str):
        super().__init__(f"orden con el id {order_id} no fue encontrado", 404, self.__class__.__name__)