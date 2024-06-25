

import json
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.plates.domain.plate import Plate
from apps.plates.domain.value_objects.ingredient_for_plate_quantity import IngredientForPlateQuantity
from apps.plates.domain.value_objects.plate_description import PlateDescription
from apps.plates.domain.value_objects.plate_id import PlateId
from apps.plates.domain.value_objects.plate_ingredient import PlateIngredient
from apps.plates.domain.value_objects.plate_name import PlateName
from apps.plates.domain.value_objects.plate_price import PlatePrice
from core.application.mappers.mapper import Mapper


class PlateMapper(Mapper[Plate, dict[str, str]]):
    def __init__(self) -> None:
        super().__init__()
    
    def from_domain_to_persistence(self, domain_entity: Plate):
        pass
    
    def from_persistence_to_domain(self, persistence_entity: dict[str, str]) -> Plate:

        ingredients = []

        for ingredient in json.loads(persistence_entity['ingredients']):
            ingredients.append({
                'ingredient_id': IngredientId(ingredient['ingredient_id']),
                'quantity': IngredientForPlateQuantity(ingredient['quantity'])
            })

        return Plate(
            PlateId(persistence_entity['id']),
            PlateName(persistence_entity['name']),
            PlateDescription(persistence_entity['description']),
            PlatePrice(persistence_entity['price']),
            [PlateIngredient(ingredient) for ingredient in ingredients]
        )