


from pydantic import BaseModel


class CreateIngredientEntry (BaseModel):
    name: str
    quantity: int