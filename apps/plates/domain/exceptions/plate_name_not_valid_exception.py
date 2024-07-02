from core.domain.exceptions.domain_exception import DomainException


class PlateNameNotValid(DomainException):
        def __init__(self): 
            msg = "Nombre del plato no válido"
            super().__init__( msg, 400, self.__class__.__name__)