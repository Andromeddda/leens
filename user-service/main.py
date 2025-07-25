from fastapi import FastAPI, Depends
from common.db import wait_for_db, SessionDep
from model.users import User, UserRole
import uuid
from typing import Optional, List

app = FastAPI()

# Wait for postgres
@app.on_event("startup")
def on_startup():
    wait_for_db()

# Create user
@app.post("/users/", response_model=User)
async def create_user(user: User, session: SessionDep):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

# Get user by UUID
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: uuid.UUID, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Get all users (filter by role optionally)
@app.get("/users/", response_model=List[User])
async def list_users(user_role: Optional[UserRole], session: SessionDep):
    # select all
    users = select(User)

    # filter optionally
    if user_role is not None:
        users = users.where(User.role == user_role)
    return session.exec(users).all()



