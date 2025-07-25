from fastapi import APIRouter, HTTPException
from sqlmodel import select
from datetime import datetime
from common.db import SessionDep
from model.order import Order, OrderStatus

router = APIRouter(prefix="/orders")

# Create order
@router.post("/", response_model=Order)
def create_order(order: Order, session: SessionDep):
    session.add(order)
    session.commit()
    session.refresh(order)
    return order

# Get all orders
@router.get("/", response_model=list[Order])
def list_orders(session: SessionDep):
    return session.exec(select(Order)).all()

# Get order by id
@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, session: SessionDep):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order

# Patch order status
@router.patch("/{order_id}/status", response_model=Order)
def update_status(order_id: int, status: OrderStatus, session: SessionDep):
    order = session.get(Order, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.status = status
    if status == OrderStatus.completed:
        order.published_at = datetime.utcnow()

    session.add(order)
    session.commit()
    session.refresh(order)
    return order