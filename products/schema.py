    # {"id": 1, "name": "Laptop", "price": 1200.99, "category": "Electronics", "in_stock": True},


from pydantic import BaseModel 

class Product(BaseModel): 
    id: int = None
    name: str
    price: float 
    category: str 
    in_stock: bool 