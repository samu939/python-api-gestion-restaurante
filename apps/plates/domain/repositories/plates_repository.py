from abc import abstractmethod
from typing import Awaitable, Optional

from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.plates.domain.plate import Plate
from apps.plates.domain.value_objects.plate_id import PlateId

class PlateRepository:
    @abstractmethod
    def get_plate_by_id(self, id: PlateId) -> Awaitable[Optional[Plate]]:
        pass
    @abstractmethod
    def get_all_plates(self) -> Awaitable[list[Plate]]:
        pass
    @abstractmethod
    def save_plate(self, plate: Plate) -> Awaitable[None]:
        pass
    @abstractmethod
    def update(self, plate: Plate) -> Awaitable[None]:
        pass
    
