from core.domain.exceptions.domain_exception import DomainException


class InventoryIdNotValid(DomainException):
        def __init__(self): 
            msg = "Id del inventario no valido"
            super().__init__( msg, 400, self.__class__.__name__)