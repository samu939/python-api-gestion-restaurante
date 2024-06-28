from core.domain.exceptions.domain_exception import DomainException


class PlateQuantityNotValid(DomainException):
        def __init__(self): 
            msg = "Debe existir una cantidad de platos"
            super().__init__(self,  msg, 400, self.__class__.__name__)