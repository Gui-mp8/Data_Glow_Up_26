from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import OrderPaymentsSchema
from app.database.models import OrderPayments
from app.database.database import get_db

order_payments_router = APIRouter()

@order_payments_router.post("/order_payments", response_model=OrderPaymentsSchema)
def add_data(payments: OrderPaymentsSchema, db : Session = Depends(get_db)):
    table = OrderPayments(**payments.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table