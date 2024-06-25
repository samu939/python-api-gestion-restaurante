from core.domain.exceptions.domain_exception import DomainException


class IngredientIdNotValid(DomainException):
        def __init__(self): 
            msg = "Id del plato no valido"
            super().__init__(self,  msg, 400, self.__class__.__name__)