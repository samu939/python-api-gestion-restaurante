from core.domain.exceptions.domain_exception import DomainException


class PlateDescriptionNotValid(DomainException):
        def __init__(self): 
            msg = "Descripción del plato no válido"
            super().__init__(self,  msg, 400, self.__class__.__name__)