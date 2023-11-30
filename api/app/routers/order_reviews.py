from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.app.routers.schemas import OrderReviewsSchema
from api.app.database.models import OrderReviews
from api.app.database.database import get_db

order_reviews_router = APIRouter()


@order_reviews_router.post("/order_reviews", response_model=OrderReviewsSchema)
def add_data(reviews: OrderReviewsSchema, db: Session = Depends(get_db)):
    table = OrderReviews(**reviews.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table
