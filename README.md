# DragonLabs Inventory Backend

A FastAPI-based backend for the DragonLabs Inventory application, providing a RESTful API to manage products with create, read, update, and delete (CRUD) operations. The backend serves the frontend React application, handling product data with a simple in-memory store and CORS support for local development.

## Features
- **RESTful API**: Supports CRUD operations for products with endpoints for listing, retrieving, creating, updating, and deleting products.
- **CORS Support**: Configured to allow requests from `http://localhost:3000` for seamless integration with the frontend.
- **Data Validation**: Uses Pydantic for robust product data validation (ID, name, description, price, quantity).
- **In-Memory Storage**: Stores product data in a list for simplicity (replaceable with a database for production).
- **Lightweight & Fast**: Built with FastAPI for high performance and automatic API documentation.

## Prerequisites
- **Python**: Version 3.8 or higher.
- **Dependencies**: FastAPI, Uvicorn, and Pydantic.
- **Frontend**: The DragonLabs Inventory frontend running at `http://localhost:3000` (optional for testing).
- **Browser or API Client**: For testing endpoints (e.g., Postman, curl, or Swagger UI).

## Installation
1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd dragonlabs-inventory-backend
   ```

2. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

4. **Set Up Files**:
   Place the following files in your project directory:
   - `main.py`: Contains the FastAPI application and API endpoints.
   - `models.py`: Defines the `Product` Pydantic model.

   Example `main.py`:
   ```python
   from fastapi import FastAPI
   from fastapi.middleware.cors import CORSMiddleware
   from models import Product

   app = FastAPI()

   origins = ["http://localhost:3000"]
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
   ```

   Example `models.py`:
   ```python
   from pydantic import BaseModel

   class Product(BaseModel):
       id: int
       name: str
       description: str
       price: float
       quantity: int
   ```

5. **Run the Application**:
   Start the FastAPI server using Uvicorn:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   The server will run at `http://localhost:8000`. The `--reload` flag enables auto-reload for development.

6. **Access API Documentation**:
   Open `http://localhost:8000/docs` in your browser to view the interactive Swagger UI for testing endpoints.

## API Endpoints
| Method | Endpoint            | Description                          | Request Body (if applicable)              | Response                             |
|--------|---------------------|--------------------------------------|------------------------------------------|--------------------------------------|
| GET    | `/products`         | Retrieve all products                | None                                     | List of products or `[]`             |
| GET    | `/products/{id}`    | Retrieve a product by ID             | None                                     | Product or `{"error": "Product not found"}` |
| POST   | `/products`         | Create a new product                 | `{"id": int, "name": str, "description": str, "price": float, "quantity": int}` | Created product                     |
| PUT    | `/products/{id}`    | Update a product by ID               | `{"id": int, "name": str, "description": str, "price": float, "quantity": int}` | Updated product or `{"error": "Product not found"}` |
| DELETE | `/products/{id}`    | Delete a product by ID               | None                                     | `{"message": "Product deleted successfully"}` or `{"error": "Product not found"}` |

### Example Request (POST `/products`):
```bash
curl -X POST "http://localhost:8000/products" -H "Content-Type: application/json" -d '{"id": 4, "name": "Headphones", "description": "Wireless headphones", "price": 199.99, "quantity": 50}'
```

### Example Response:
```json
{
  "id": 4,
  "name": "Headphones",
  "description": "Wireless headphones",
  "price": 199.99,
  "quantity": 50
}
```

## File Structure
```
dragonlabs-inventory-backend/
├── main.py               # FastAPI application with API endpoints
├── models.py             # Pydantic model for Product
├── requirements.txt      # (Optional) List of dependencies
└── README.md             # This file
```

Optional `requirements.txt`:
```
fastapi
uvicorn
pydantic
```

## Usage
1. **Start the Server**: Run `uvicorn main:app --reload --host 0.0.0.0 --port 8000`.
2. **Test Endpoints**: Use the Swagger UI at `http://localhost:8000/docs` or tools like Postman to interact with the API.
3. **Integrate with Frontend**: Ensure the frontend (e.g., DragonLabs Inventory React app) is configured to make requests to `http://localhost:8000`.
4. **Manage Products**: The API supports CRUD operations, with initial sample data for a laptop, smartphone, and tablet.

## Notes
- **Storage**: The backend uses an in-memory list (`products`) for simplicity. For production, replace with a database like PostgreSQL or MongoDB.
- **CORS**: Configured to allow requests from `http://localhost:3000`. Update the `origins` list in `main.py` if the frontend is hosted elsewhere.
- **Error Handling**: Returns appropriate error messages for invalid IDs or failed operations.
- **Production**: For production, remove `--reload`, use a production-grade server (e.g., Gunicorn + Uvicorn), and secure the API with authentication.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for bugs, features, or improvements.

## License
This project is licensed under the MIT License.

---
*Built with 💜 by DragonLabs*