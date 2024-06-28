
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_quantity import PlateQuantity

class CookPlateDto:
    
    def __init__(self, plate_id: PlateId ,quantity: PlateQuantity) -> None:
        self.plate_id = plate_id 
        self.quantity = quantity 