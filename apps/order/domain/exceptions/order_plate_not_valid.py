from core.domain.exceptions.domain_exception import DomainException


class OrderPlateNotValid(DomainException):
        def __init__(self): 
            msg = "plato no válido"
            super().__init__(  msg, 400, self.__class__.__name__)