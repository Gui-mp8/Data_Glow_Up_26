from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import GeolocationSchema
from app.database.models import Geolocation
from app.database.database import get_db

geolocation_router = APIRouter()

@geolocation_router.post("/geolocation", response_model=GeolocationSchema)
def add_data(geolocation: GeolocationSchema, db : Session = Depends(get_db)):
    table = Geolocation(**geolocation.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table