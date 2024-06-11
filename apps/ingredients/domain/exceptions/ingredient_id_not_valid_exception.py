from core.domain.exceptions.domain_exception import DomainException


class IngredientIdNotValid(DomainException):
        def __init__(self): 
            msg = "Id del ingrediente no valido"
            super().__init__(self,  msg)