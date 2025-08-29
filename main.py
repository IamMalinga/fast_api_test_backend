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
)

products = [
    Product(id=1, name="Laptop", description="A high performance laptop", price=999.99, quantity=10),
    Product(id=2, name="Smartphone", description="A latest model smartphone", price=599.99, quantity=20),
    Product(id=3, name="Tablet", description="A lightweight tablet", price=399.99, quantity=15)
]

@app.get("/products")
def read_root():
    return products   