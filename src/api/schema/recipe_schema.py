from pydantic import BaseModel


class Recipe(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
