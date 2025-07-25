from fastapi import APIRouter, HTTPException
from sqlmodel import select
from common.db import SessionDep
from model.channel import Channel

router = APIRouter(prefix="/channels")

# Create channel
@router.post("/", response_model=Channel)
def create_channel(channel: Channel, session: SessionDep):
    session.add(channel)
    session.commit()
    session.refresh(channel)
    return channel

# Get all channels
@router.get("/", response_model=list[Channel])
def list_channels(session: SessionDep):
    return session.exec(select(Channel)).all()

# Get channel by id
@router.get("/{channel_id}", response_model=Channel)
def get_channel(channel_id: int, session: SessionDep):
    channel = session.get(Channel, channel_id)
    if not channel:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channel