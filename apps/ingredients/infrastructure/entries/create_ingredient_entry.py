


from pydantic import BaseModel


class CreateIngredientEntry (BaseModel):
    name: str
    quantity: float
    store_id: str