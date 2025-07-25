from sqlmodel import SQLModel, Field
from datetime import datetime

import uuid

# Media channel owned by user
class Channel(SQLModel, table=True):
    id:         int | None  = Field(default=None, primary_key=True)
    owner_id:   uuid.UUID   = Field()
    title:      str         = Field()
    theme:      str         = Field()
    price:      int         = Field()
    subscribers: int        = Field()
    link:       str         = Field()