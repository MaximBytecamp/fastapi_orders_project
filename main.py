from fastapi import FastAPI

from app.routers.orders import router 


app = FastAPI(
    title="Order Pickup Point API",
    description=(
        "API пункта выдали интернет-магазина"
    ),
    version="1.0.0"
)

app.include_router(router)


