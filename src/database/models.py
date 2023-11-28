from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(String(32), primary_key=True)
    customer_unique_id = Column(String(32))
    customer_zip_code_prefix = Column(String(5))
    customer_city = Column(String(50))
    customer_state = Column(String(2))

class Geolocation(Base):
    __tablename__ = 'geolocation'
    __mapper_args__ = {
        "primary_key": ["geolocation_zip_code_prefix"]
    }
    # geolocation_id = Column(String(36), primary_key=True)
    geolocation_zip_code_prefix = Column(String(5))
    geolocation_lat = Column(Float)
    geolocation_lng = Column(Float)
    geolocation_city = Column(String(50))
    geolocation_state = Column(String(2))

class Orders(Base):
    __tablename__ = 'orders'
    order_id = Column(String(32), primary_key=True)
    customer_id = Column(String(32), ForeignKey('customers.customer_id'))
    order_status = Column(String(15))
    order_purchase_timestamp = Column(DateTime)
    order_delivered_carrier_date = Column(DateTime)
    order_delivered_customer_date = Column(DateTime)
    order_estimated_delivery_date = Column(DateTime)

class Products(Base):
    __tablename__ = 'products'
    product_id = Column(String(32), primary_key=True)
    product_category_name = Column(String(100))
    product_name_lenght = Column(Integer)
    product_description_lenght = Column(Integer)
    product_photos_qty = Column(Integer)
    product_weight_g = Column(Integer)
    product_length_cm = Column(Integer)
    product_height_cm = Column(Integer)
    product_width_cm = Column(Integer)

class Sellers(Base):
    __tablename__ ='sellers'
    seller_id = Column(String(32), primary_key=True)
    seller_zip_code_prefix = Column(String(5))
    seller_city = Column(String(100))
    seller_state = Column(String(2))

class OrderItems(Base):
    __tablename__ = 'order_items'
    __mapper_args__ = {
        "primary_key": ["order_item_id"]
    }
    order_id = Column(String(32), ForeignKey('orders.order_id'))
    order_item_id = Column(Integer)
    # order_item_id = Column(Integer, primary_key=True)
    product_id = Column(String(32), ForeignKey('products.product_id'))
    seller_id = Column(String(32), ForeignKey('sellers.seller_id'))
    shipping_limit_date = Column(DateTime)
    price = Column(Float)
    freight_value = Column(Float)

class OrderPayments(Base):
    __tablename__ = 'order_payments'
    __mapper_args__ = {
        "primary_key": ["payment_sequential"]
    }
    # payment_id = Column(Integer, primary_key=True)
    order_id = Column(String(32), ForeignKey('orders.order_id'))
    payment_sequential = Column(Integer)
    payment_type = Column(String(20))
    payment_installments = Column(Integer)
    payment_value = Column(Float)

class OrderReviews(Base):
    __tablename__ = 'order_reviews'
    review_id = Column(String(32), primary_key=True)
    order_id = Column(String(32), ForeignKey('orders.order_id'))
    review_score = Column(Integer)
    review_comment_title = Column(Text)
    review_comment_message = Column(Text)
    review_creation_date = Column(DateTime)
    review_answer_timestamp = Column(DateTime)

class ProductCategoryNameTranslation(Base):
    __tablename__ = 'product_category_name_translation'
    __mapper_args__ = {
        "primary_key": ["product_category_name"]
    }
    # product_category_name_id = Column(Integer, primary_key=True)
    product_category_name = Column(String(100))
    product_category_name_english = Column(String(100))

class ClosedDeals(Base):
    __tablename__ = 'closed_deals'
    __mapper_args__ = {
        "primary_key": ["sdr_id"]
    }
    # closed_deal_id = Column(Integer, primary_key=True)
    mql_id = Column(String(32), ForeignKey('marketing_qualified_leads.mql_id'))
    seller_id = Column(String(32), ForeignKey('sellers.seller_id'))
    sdr_id = Column(String(32))
    sr_id = Column(String(32))
    won_date = Column(DateTime)
    business_segment = Column(String(100))
    lead_type = Column(String (20))
    lead_behaviour_profile = Column(String(30))
    has_company = Column(Boolean)
    has_gtin = Column(Boolean)
    average_stock = Column(String(10))
    business_type = Column(String(20))
    declared_product_catalog_size = Column(Float)
    declared_monthly_revenue = Column(Float)

class MarketingQualifiedLeads(Base):
    __tablename__ ='marketing_qualified_leads'
    mql_id = Column(String(32), primary_key=True)
    first_contact_date = Column(Date)
    landing_page_id = Column(String(32))
    origin = Column(String(30))
