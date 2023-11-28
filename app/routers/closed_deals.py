from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import ClosedDealsSchema
from app.database.models import ClosedDeals
from app.database.database import get_db

closed_deals_router = APIRouter()

@closed_deals_router.post("/closed_deals", response_model=ClosedDealsSchema)
def add_data(closed_deals: ClosedDealsSchema, db : Session = Depends(get_db)):
    table = ClosedDeals(**closed_deals.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table