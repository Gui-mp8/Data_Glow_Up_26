from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.app.routers.schemas import ProductsSchema
from api.app.database.models import Products
from api.app.database.database import get_db

products_router = APIRouter()


@products_router.post("/products", response_model=ProductsSchema)
def add_customers(products: ProductsSchema, db: Session = Depends(get_db)):
    table = Products(**products.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table
