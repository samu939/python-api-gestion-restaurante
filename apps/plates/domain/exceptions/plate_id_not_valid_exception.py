from core.domain.exceptions.domain_exception import DomainException


class PlateIdNotValid(DomainException):
        def __init__(self): 
            msg = "Id del plato no válido"
            super().__init__(  msg, 400, self.__class__.__name__)