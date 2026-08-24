from pydantic import BaseModel, Field 
from app.storage import OrderStatus

class Order(BaseModel):
    id: int 
    customer: str
    product: str 
    status: OrderStatus