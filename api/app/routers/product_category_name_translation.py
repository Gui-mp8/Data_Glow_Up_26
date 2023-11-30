from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.app.routers.schemas import ProductCategoryNameTranslationSchema
from api.app.database.models import ProductCategoryNameTranslation
from api.app.database.database import get_db

product_category_name_translation_router = APIRouter()


@product_category_name_translation_router.post(
    "/product_category_name_translation",
    response_model=ProductCategoryNameTranslationSchema,
)
def add_data(
    product_category_name_translation: ProductCategoryNameTranslationSchema,
    db: Session = Depends(get_db),
):
    table = ProductCategoryNameTranslation(
        **product_category_name_translation.model_dump()
    )
    db.add(table)
    db.commit()
    db.refresh(table)
    return table
