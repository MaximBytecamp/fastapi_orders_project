from fastapi import APIRouter, HTTPException, status 

from app import storage 
from app.schemas import Order

router = APIRouter()

@router.get("/orders", response_model=list[Order], tags=["Заказы"])
def get_orders() -> list[dict]:
    return storage.orders 