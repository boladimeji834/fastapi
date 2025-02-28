from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from schemas import CategoryURLChoices, Product


app = FastAPI()
products = [
    {"id": 1, "name": "Laptop", "price": 750.00, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Smartphone", "price": 500.00, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Coffee Maker", "price": 80.00, "category": "Home Appliances", "in_stock": False},
    {"id": 4, "name": "Desk Chair", "price": 150.00, "category": "Furniture", "in_stock": True},
    {"id": 5, "name": "Headphones", "price": 120.00, "category": "Electronics", "in_stock": False},
    {"id": 6, "name": "Electric Kettle", "price": 40.00, "category": "Home Appliances", "in_stock": True},
    {"id": 7, "name": "Tablet", "price": 300.00, "category": "Electronics", "in_stock": True},
    {"id": 8, "name": "Office Desk", "price": 200.00, "category": "Furniture", "in_stock": False},
    {"id": 9, "name": "Wireless Mouse", "price": 25.00, "category": "Accessories", "in_stock": True},
    {"id": 10, "name": "Keyboard", "price": 35.00, "category": "Accessories", "in_stock": True},
]

# Trying the Enum class to prevent just any kind of input




@app.get("/")
async def home() -> dict: 
    return {"message": "Welcome to the homepage!"}

# testing query parameters on the products api 
@app.get("/products")
async def product(id: int = None, in_stock: str = None) -> list[Product]: 
    if id: 
        return [
            Product(**prod) for prod in products if prod["id"] == id
        ]

    if in_stock: 
        return [
            Product(**prod) for prod in products if prod["in_stock"] == True
        ]
    return [
        Product(**product) for product in products
    ]



@app.get("/product/{product_id}")
async def post(product_id: int):
    prod = next((Product(**prod) for prod in products if prod["id"] == product_id), None)
    if not prod: 
        raise HTTPException(status_code=404, detail="Product not found")
    return prod


@app.get("/product/category/{prod_cat}")
async def get_by_cat(prod_cat: CategoryURLChoices) -> Product: 
    return [
        Product(**prod) for prod in products if prod["category"].lower() == prod_cat.value.lower()
    ]

