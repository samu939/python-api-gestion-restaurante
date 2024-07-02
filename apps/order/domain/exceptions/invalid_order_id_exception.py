from core.domain.exceptions.domain_exception import DomainException


class OrderIdNotValid(DomainException):
        def __init__(self): 
            msg = "Id de la orden no válido"
            super().__init__(  msg, 400, self.__class__.__name__)