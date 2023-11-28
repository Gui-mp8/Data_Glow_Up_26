from typing import Optional

from pydantic import BaseModel

class CustomersSchema(BaseModel):
    customer_id : str
    customer_unique_id : str
    customer_zip_code_prefix : Optional[str] = None
    customer_city : Optional[str] = None
    customer_state : Optional[str] = None