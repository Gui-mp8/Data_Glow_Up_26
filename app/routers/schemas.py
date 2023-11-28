from typing import Optional

from pydantic import BaseModel, constr

class CustomersSchema(BaseModel):
    customer_id: constr(min_length=32, max_length=32)
    customer_unique_id: constr(min_length=32, max_length=32)
    customer_zip_code_prefix: Optional[str] = None
    customer_city: Optional[str] = None
    customer_state: Optional[str] = None
