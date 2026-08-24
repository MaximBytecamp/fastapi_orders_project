from fastapi import APIRouter, HTTPException, status 

from app import storage 
from app.schemas import Order, OrderCreate, Message

router = APIRouter()

@router.get("/orders", response_model=list[Order], tags=["Заказы"])
def get_orders() -> list[dict]:
    return storage.orders 


@router.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED, tags=["Заказы"])
def create_order(order_data: OrderCreate) -> dict:
    return storage.add_order(order_data.customer, order_data.product)


@router.delete("/orders/{order_id}", response_model=Message, tags=["Заказы"])
def delete_order(order_id: int) -> dict:
    order = storage.find_order(order_id)
    storage.remove_order(order)
    return {"message": "Заказ удален"}