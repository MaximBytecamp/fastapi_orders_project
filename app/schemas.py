from pydantic import BaseModel, Field 
from app.storage import OrderStatus

class Order(BaseModel):
    id: int 
    customer: str
    product: str 
    status: OrderStatus

class OrderCreate(BaseModel):
    customer: str = Field(min_length=1, examples=["Иван"])
    product: str = Field(min_length=1, examples=["Мышь"])


class Message(BaseModel):
    message: str 