from fastapi import FastAPI

from app.routers.closed_deals import closed_deals_router
from app.routers.customers import customers_router
from app.routers.geolaction import geolocation_router
from app.routers.marketing_qualified_leads import marketing_qualified_leads_router
from app.routers.order_items import order_items_router
from app.routers.order_payments import order_payments_router
from app.routers.order_reviews import order_reviews_router
from app.routers.orders import orders_router
from app.routers.product_category_name_translation import product_category_name_translation_router
from app.routers.products import products_router
from app.routers.sellers import sellers_router
from app.database import models
from app.database.database import engine

models.Base.metadata.drop_all(bind=engine)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(closed_deals_router)
app.include_router(customers_router)
app.include_router(geolocation_router)
app.include_router(marketing_qualified_leads_router)
app.include_router(order_items_router)
app.include_router(order_payments_router)
app.include_router(order_reviews_router)
app.include_router(orders_router)
app.include_router(product_category_name_translation_router)
app.include_router(products_router)
app.include_router(sellers_router)


