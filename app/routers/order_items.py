from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import OrderItemsSchema
from app.database.models import OrderItems
from app.database.database import get_db

order_items_router = APIRouter()

@order_items_router.post("/order_items", response_model=OrderItemsSchema)
def add_data(order_items: OrderItemsSchema, db : Session = Depends(get_db)):
    table = OrderItems(**order_items.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table