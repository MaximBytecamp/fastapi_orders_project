from fastapi import APIRouter, HTTPException, status 

from app import storage 
from app.schemas import Order, OrderCreate, Message, StatusUpdate
from app.storage import OrderStatus
router = APIRouter()

def get_order_or_404(order_id: int) -> dict:
    order = storage.find_order(order_id)

    if order is None: 
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="Заказ не найден"
        )

    return order

@router.get("/status/{order_status}", response_model=list[Order], tags=["Поиск"])
def get_orders_by_status(order_status: OrderStatus) -> list[dict]:
    return [order for order in storage.orders if order["status"] == order_status]


@router.get("/orders", response_model=list[Order], tags=["Заказы"])
def get_orders() -> list[dict]:
    return storage.orders 


@router.post("/orders", response_model=Order, status_code=status.HTTP_201_CREATED, tags=["Заказы"])
def create_order(order_data: OrderCreate) -> dict:
    return storage.add_order(order_data.customer, order_data.product)


@router.delete("/orders/{order_id}", response_model=Message, tags=["Заказы"])
def delete_order(order_id: int) -> dict:
    order = get_order_or_404(order_id)
    storage.remove_order(order)
    return {"message": "Заказ удален"}


@router.get("/customer/{customer}", response_model = list[Order], tags = ["Поиск"])
def get_orders_by_customer(customer: str) -> list[dict]:
    normal_customer = customer.casefold()

    return [order for order in storage.orders if order["customer"].casefold() == normal_customer]


@router.patch("/{order_id}/status", response_model= Order, tags=["Заказы"])
def update_status(order_id: int, data: StatusUpdate) -> dict:
    order = get_order_or_404(order_id)
    order["status"] = data.status 
    return order 
