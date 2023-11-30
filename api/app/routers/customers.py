from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.app.routers.schemas import CustomersSchema
from api.app.database.models import Customers
from api.app.database.database import get_db

customers_router = APIRouter()


@customers_router.post("/customers", response_model=CustomersSchema)
def add_data(customers: CustomersSchema, db: Session = Depends(get_db)):
    table = Customers(**customers.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table
