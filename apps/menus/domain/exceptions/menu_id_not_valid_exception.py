from core.domain.exceptions.domain_exception import DomainException


class MenuIdNotValid(DomainException):
        def __init__(self): 
            msg = "Id del menú no válido"
            super().__init__(  msg, 400, self.__class__.__name__)