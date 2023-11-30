from typing import Optional
from datetime import datetime, date

from pydantic import BaseModel, constr, field_validator


class CustomersSchema(BaseModel):
    customer_id: constr(min_length=32, max_length=32)
    customer_unique_id: constr(min_length=32, max_length=32)
    customer_zip_code_prefix: Optional[str] = None
    customer_city: Optional[str] = None
    customer_state: Optional[str] = None


class GeolocationSchema(BaseModel):
    geolocation_zip_code_prefix: str
    geolocation_lat: float
    geolocation_lng: float
    geolocation_city: Optional[str] = None
    geolocation_state: Optional[str] = None


class OrdersSchema(BaseModel):
    order_id: constr(min_length=32, max_length=32)
    customer_id: constr(min_length=32, max_length=32)
    order_status: str
    order_purchase_timestamp: datetime
    order_delivered_carrier_date: datetime
    order_delivered_customer_date: datetime
    order_estimated_delivery_date: datetime


class ProductsSchema(BaseModel):
    product_id: constr(min_length=32, max_length=32)
    product_category_name: Optional[str] = None
    product_name_lenght: Optional[int] = None
    product_description_lenght: Optional[int] = None
    product_photos_qty: Optional[int] = None
    product_weight_g: Optional[int] = None
    product_length_cm: Optional[int] = None
    product_height_cm: Optional[int] = None
    product_width_cm: Optional[int] = None


class SellersSchema(BaseModel):
    seller_id: constr(min_length=32, max_length=32)
    seller_zip_code_prefix: Optional[str] = None
    seller_city: Optional[str] = None
    seller_state: Optional[str] = None


class OrderItemsSchema(BaseModel):
    order_id: constr(min_length=32, max_length=32)
    order_item_id: int
    product_id: constr(min_length=32, max_length=32)
    seller_id: constr(min_length=32, max_length=32)
    shipping_limit_date: datetime
    price: float
    freight_value: float


class OrderPaymentsSchema(BaseModel):
    order_id: constr(min_length=32, max_length=32)
    payment_sequential: int
    payment_type: Optional[str] = None
    payment_installments: int
    payment_value: float


class OrderReviewsSchema(BaseModel):
    review_id: constr(min_length=32, max_length=32)
    order_id: constr(min_length=32, max_length=32)
    review_score: Optional[int] = None
    review_comment_title: Optional[str] = None
    review_comment_message: Optional[str] = None
    review_creation_date: datetime
    review_answer_timestamp: datetime


class ProductCategoryNameTranslationSchema(BaseModel):
    product_category_name: str
    product_category_name_english: str


class ClosedDealsSchema(BaseModel):
    mql_id: constr(min_length=32, max_length=32)
    seller_id: constr(min_length=32, max_length=32)
    sdr_id: constr(min_length=32, max_length=32)
    sr_id: constr(min_length=32, max_length=32)
    won_date: datetime
    business_segment: Optional[str] = None
    lead_type: Optional[str] = None
    lead_behaviour_profile: Optional[str] = None
    has_company: Optional[bool] = None
    has_gtin: Optional[bool] = None
    average_stock: Optional[str] = None
    business_type: Optional[str] = None
    declared_product_catalog_size: Optional[float] = None
    declared_monthly_revenue: Optional[float] = 0.0


class MarketingQualifiedLeadsSchema(BaseModel):
    mql_id: constr(min_length=32, max_length=32)
    first_contact_date: Optional[date] = datetime.now().date()
    landing_page_id: constr(min_length=32, max_length=32)
    origin: Optional[str] = None

    @field_validator("first_contact_date")
    def set_default_date(cls, value):
        return value or datetime.now().date()
