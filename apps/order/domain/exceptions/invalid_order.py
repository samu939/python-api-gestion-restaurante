from core.domain.exceptions.domain_exception import DomainException


class OrderNotValid(DomainException):
        def __init__(self): 
            msg = "orden no valida"
            super().__init__(  msg, 400, self.__class__.__name__)