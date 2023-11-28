from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import CustomersSchema
from app.database.models import Customers
from app.database.database import get_db

customers_router = APIRouter()

@customers_router.post("/customers", response_model=CustomersSchema)
def add_customers(customers: CustomersSchema, db : Session = Depends(get_db)):
    db_customers = Customers(**customers.model_dump())
    db.add(db_customers)
    db.commit()
    db.refresh(db_customers)
    return db_customers