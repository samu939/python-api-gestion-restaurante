from core.domain.exceptions.domain_exception import DomainException

class InvalidUserException(DomainException):
    def __init__(self):
        super().__init__("usuario no valido", 400, self.__class__.__name__)
