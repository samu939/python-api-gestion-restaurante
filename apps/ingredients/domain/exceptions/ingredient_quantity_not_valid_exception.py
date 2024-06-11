from core.domain.exceptions.domain_exception import DomainException


class IngredientQuantityNotValid(DomainException):
        def __init__(self): 
            msg = "Cantidad del ingrediente no valida"
            super().__init__(self,  msg)