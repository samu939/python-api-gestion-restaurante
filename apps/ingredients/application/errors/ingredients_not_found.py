from apps.ingredients.domain.value_objects.ingredient_id import IngredientId
from core.application.errors.application_errors import ApplicationError

class IngredientsNotFoundApplicatonError(ApplicationError):
    def __init__(self, ingredient_id: IngredientId):
        super().__init__(f"ingrediente con el id {ingredient_id.value} no fue encontrado", 404, self.__class__.__name__)