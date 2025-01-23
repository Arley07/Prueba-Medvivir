from fastapi import FastAPI
from app.routers import products

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API"}

app.include_router(products.router)