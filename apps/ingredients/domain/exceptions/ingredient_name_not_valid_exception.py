from core.domain.exceptions.domain_exception import DomainException


class IngredientNameNotValid(DomainException):
        def __init__(self): 
            msg = "Nombre del ingrediente no valido"
            super().__init__(self,  msg)