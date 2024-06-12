from core.domain.exceptions.domain_exception import DomainException


class IngredientQuantityNotValid(DomainException):
        def __init__(self): 
            msg = "cantidad del ingrediente no valida"
            super().__init__(self,  msg, 400, self.__class__.__name__)