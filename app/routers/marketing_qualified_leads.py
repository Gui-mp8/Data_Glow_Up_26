from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers.schemas import MarketingQualifiedLeadsSchema
from app.database.models import MarketingQualifiedLeads
from app.database.database import get_db

marketing_qualified_leads_router = APIRouter()

@marketing_qualified_leads_router.post("/marketing_qualified_leads", response_model=MarketingQualifiedLeadsSchema)
def add_data(marketing: MarketingQualifiedLeadsSchema, db : Session = Depends(get_db)):
    table = MarketingQualifiedLeads(**marketing.model_dump())
    db.add(table)
    db.commit()
    db.refresh(table)
    return table