from core.domain.exceptions.domain_exception import DomainException


class OrderDateNotValid(DomainException):
        def __init__(self): 
            msg = "fecha de la orden no valida"
            super().__init__(self,  msg, 400, self.__class__.__name__)