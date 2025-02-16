
from fastapi import FastAPI
from schema import Product
from typing import Optional, List


app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 1200.99, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Coffee Maker", "price": 80.50, "category": "Appliances", "in_stock": False},
    {"id": 3, "name": "Smartphone", "price": 699.99, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "Air Conditioner", "price": 450.00, "category": "Appliances", "in_stock": True},
    {"id": 5, "name": "Desk Chair", "price": 150.25, "category": "Furniture", "in_stock": True},
    {"id": 6, "name": "Notebook", "price": 5.99, "category": "Stationery", "in_stock": True},
    {"id": 7, "name": "Gaming Console", "price": 299.99, "category": "Electronics", "in_stock": False},
    {"id": 8, "name": "Vacuum Cleaner", "price": 120.00, "category": "Appliances", "in_stock": True},
    {"id": 9, "name": "Office Desk", "price": 300.00, "category": "Furniture", "in_stock": False},
    {"id": 10, "name": "Pen", "price": 1.99, "category": "Stationery", "in_stock": True}
]

@app.get("/")
def home(): 
    return {
        "message": "You're welcome to the home page!"
    }



# 6. Get Products Priced Above a Certain Threshold
@app.get("/products/")
async def filter_products(
    in_stock: Optional[bool] = None, 
    category: Optional[str] = None, 
    price_threshold: Optional[int] = None
) -> List[Product]: 
    filtered_prods = products

    if in_stock is not None: 
        filtered_prods = [prod for prod in products if prod["in_stock"] == in_stock]
    
    if category is not None: 
        filtered_prods = [prod for prod in products if prod["category"].lower() == category.lower()]
    
    if price_threshold is not None: 
        filtered_prods = [prod for prod in products if prod["price"] > price_threshold]
    
    return [
        Product(**prod) for prod in filtered_prods 
    ]

@app.get("/product/")
async def filter_by_id(id: int) -> Product: 
    return [Product(**prod) for prod in products if prod["id"] == id][0]

@app.get("/sorted-products-by-price")
async def sorted_products(): 
    return sorted(products, key=lambda x: x["price"])

@app.get("/products/average-of-prices")
async def get_sum(): 
    avg = sum([prod["price"] for prod in products]) / len(products)
    return {"average-price": avg}


# add a new product 
@app.post("/products/{ops})")
async def add_product(product: Product): 
        last_id = max([prod["id"] for prod in products])
        product = product.dict()
        product["id"] = last_id + 1
        products.append(product)
        return {"message": "Product has been added"}


@app.post("/products/update")
async def update_product(id: int, item: Product): 
    for prod in products: 
        if prod["id"] == id: 
            prod = item
    else: print("Product updated successfully!")

    return {"message": "Product updated successfully!"}

# delete a product 
@app.post("/products/delete")
async def delete_post(id: int): 
    new_prods = [prod for prod in products if prod["id"] != id]
    products = new_prods

    return {"message": "Product deleted successfully!"}