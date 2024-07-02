from core.domain.exceptions.domain_exception import DomainException


class OrderPriceNotValid(DomainException):
        def __init__(self): 
            msg = "precio de la orden no valido"
            super().__init__(  msg, 400, self.__class__.__name__)