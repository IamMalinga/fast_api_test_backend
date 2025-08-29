from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Product

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],          
    allow_headers=["*"],   
)

products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=599.99, quantity=20),
    Product(id=3, name="Tablet", description="A lightweight tablet", price=399.99, quantity=15)
]

@app.get("/products")
def read_root():
    return products   


@app.get("/products/{id}")
def read_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    for index, p in enumerate(products):
        if p.id == id:
            products[index] = product
            return product
    return {"error": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int):
    for index, p in enumerate(products):
        if p.id == id:
            del products[index]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}