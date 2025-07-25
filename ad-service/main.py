from fastapi import FastAPI
from common.db import wait_for_db
from route import channels, orders

app = FastAPI()

app.include_router(channels.router)
app.include_router(orders.router)

@app.on_event("startup")
def on_startup():
    wait_for_db()
