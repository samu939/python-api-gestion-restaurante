from core.domain.exceptions.domain_exception import DomainException


class MenuNameNotValid(DomainException):
        def __init__(self): 
            msg = "Nombre del Menú no válido"
            super().__init__(  msg, 400, self.__class__.__name__)