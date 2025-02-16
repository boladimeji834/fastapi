from enum import Enum 

class CategoryURLChoices(Enum): 
    electronics = "electronics"
    beverages = "bevarages"
    accessories = "Accessories"
    furniture = "furniture"
    home_appliances = "home Appliances"


    # {"id": 1, "name": "Laptop", "price": 750.00, "category": "Electronics", "in_stock": True},
from pydantic import BaseModel

class Product(BaseModel): 
    id: int
    name: str
    price: float 
    category: str 
    in_stock: bool 

