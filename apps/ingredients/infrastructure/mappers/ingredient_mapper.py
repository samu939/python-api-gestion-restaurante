from apps.ingredients.domain.ingredient import Ingredient
from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from apps.ingredients.domain.value_objects.ingredient_name import IngredientName
from apps.ingredients.domain.value_objects.ingredient_quantity import IngredientQuantity
from core.application.mappers.mapper import Mapper

class IngredientMapper(Mapper[Ingredient, dict[str, str]]):
    def __init__(self) -> None:
        super().__init__()

    def from_domain_to_persistence(self, domain_entity: Ingredient) -> dict[str, str]:
        return {
            'id': domain_entity.id.value,
            'name': domain_entity.name.value,
            'quantity': domain_entity.quantity.value
        }

    def from_persistence_to_domain(self, persistence_entity: dict[str, str]) -> Ingredient:
        return Ingredient(
            IngredientId(persistence_entity['id']),
            IngredientName(persistence_entity['name']),
            IngredientQuantity(persistence_entity['quantity'])
        )