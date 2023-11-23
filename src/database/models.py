from sqlalchemy import Column, String, Date, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customers(Base):
    customer_id = Column(String(32), primary_key=True)
    customer_unique_id = Column(String(32), primary_key=True)
    customer_zip_code_prefix = Column(String(5))
    customer_city = Column(String())
    customer_state = Column(String(2))

