from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.app.routers.schemas import SellersSchema
from api.app.database.models import Sellers
from api.app.database.database import get_db

sellers_router = APIRouter()


@sellers_router.post("/sellers", response_model=SellersSchema)
def add_data(sellers: SellersSchema, db: Session = Depends(get_db)):
    table = Sellers(**sellers.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table
