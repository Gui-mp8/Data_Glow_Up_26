from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import OrdersSchema
from app.database.models import Orders
from app.database.database import get_db

orders_router = APIRouter()

@orders_router.post("/orders", response_model=OrdersSchema)
def add_data(orders: OrdersSchema, db : Session = Depends(get_db)):
    table = Orders(**orders.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table