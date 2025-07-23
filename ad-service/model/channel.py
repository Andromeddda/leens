from sqlmodel import SQLModel, Field
from datetime import datetime

class Channel(SQLModel, table=True):
    id:         int | None  = Field(default=None, primary_key=True)
    owner_id:   int         = Field(foreign_key = "user.id")
    title:      str         = Field()
    theme:      str         = Field()
    price:      int         = Field()
    subscribers: int        = Field()
    link:       str         = Field()