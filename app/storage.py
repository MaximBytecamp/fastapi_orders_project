from copy import deepcopy 
from enum import Enum

class OrderStatus(str, Enum):
    created = "created"
    ready = "ready"
    issued = "issued"

INITIAL_ORDERS: list[dict] = [
    {
        "id": 1,
        "customer": "Анна",
        "product": "Клавиатура",
        "status": OrderStatus.ready
    },
    {
        "id": 2,
        "customer": "Игорь",
        "product": "Наушники",
        "status": OrderStatus.created
    }
]

orders: list[dict] = deepcopy(INITIAL_ORDERS)
next_order_id = 3 


def add_order(customer: str, product: str) -> dict:
    global next_order_id

    new_order = {
        "id": next_order_id,
        "customer": customer,
        "product": product,
        "status": OrderStatus.created 
    }

    next_order_id += 1
    orders.append(new_order)
    return new_order

def remove_order(order: dict) -> None:
    orders.remove(order)


def find_order(order_id: int) -> dict | None: 
    for order in orders: 
        if order["id"] == order_id:
            return order 

    return None 