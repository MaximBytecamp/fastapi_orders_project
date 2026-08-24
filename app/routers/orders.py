from fastapi import APIRouter, HTTPException, status 

from app import storage 

router = APIRouter()

@router.get("/orders")
def get_orders() -> list[dict]:
    return storage.orders 