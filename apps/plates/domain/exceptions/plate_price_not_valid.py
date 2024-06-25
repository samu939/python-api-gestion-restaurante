from core.domain.exceptions.domain_exception import DomainException


class PlatePriceNotValid(DomainException):
        def __init__(self): 
            msg = "precio del plato no valida"
            super().__init__(self,  msg, 400, self.__class__.__name__)