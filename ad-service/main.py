from fastapi import FastAPI

from common.db import wait_for_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    wait_for_db()
