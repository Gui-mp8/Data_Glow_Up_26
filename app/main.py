from fastapi import FastAPI

from app.routers.customers import customers_router
from app.database import models
from app.database.database import engine

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(customers_router)
