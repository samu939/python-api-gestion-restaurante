from core.domain.exceptions.domain_exception import DomainException


class OrderPlateQuantityNotValid(DomainException):
        def __init__(self): 
            msg = "cantidad de platos no valida"
            super().__init__(  msg, 400, self.__class__.__name__)