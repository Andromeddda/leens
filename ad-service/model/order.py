from sqlmodel import SQLModel, Field
from datetime import datetime
from enum import Enum
import uuid

class OrderStatus(str, Enum):
    pending = "pending"
    declined = "declined"
    completed = "completed"

# Request to buy ad from advertiser
class Order(SQLModel, table = True):
    id:             int | None      = Field(default = None, primary_key = True)
    channel_id:     int             = Field(foreign_key = "channel.id")
    advertiser_id:  uuid.UUID       = Field()
    status:         OrderStatus     = Field(default = OrderStatus.pending)
    created_at:     datetime        = Field(default_factory = datetime.utcnow)
    published_at:   datetime | None = Field(default = None)
    message_text:   str             = Field(default = None)