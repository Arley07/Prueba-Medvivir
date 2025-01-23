from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

FAKE_STORE_API_URL = "https://fakestoreapi.com/products"

@router.get("/products/{page}/{limit}")
def get_products(page: int, limit: int):
    response = requests.get(FAKE_STORE_API_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching products")
    products = response.json()
    start = (page - 1) * limit
    end = start + limit
    return products[start:end]

@router.get("/products/{product_id}")
def get_product(product_id: int):
    response = requests.get(f"{FAKE_STORE_API_URL}/{product_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Product not found")
    return response.json()

@router.get("/products/category/{category}")
def get_products_by_category(category: str):
    response = requests.get(f"{FAKE_STORE_API_URL}/category/{category}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Category not found")
    return response.json()

@router.get("/products/search")
def search_products(name: str):
    response = requests.get(FAKE_STORE_API_URL)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching products")
    products = response.json()
    return [product for product in products if name.lower() in product["title"].lower()]

@router.post("/products")
def create_product(product: dict):
    response = requests.post(FAKE_STORE_API_URL, json=product)
    if response.status_code != 201:
        raise HTTPException(status_code=response.status_code, detail="Error creating product")
    return response.json()

@router.put("/products/{product_id}")
def update_product(product_id: int, product: dict):
    response = requests.put(f"{FAKE_STORE_API_URL}/{product_id}", json=product)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error updating product")
    return response.json()

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    response = requests.delete(f"{FAKE_STORE_API_URL}/{product_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error deleting product")
    return {"message": "Product deleted successfully"}
