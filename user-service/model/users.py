from sqlmodel import Field, SQLModel
from enum import Enum
import uuid

class UserRole(str, Enum):
    advertiser = "advertiser"
    client = "client"

class User(SQLModel, table=True):
    id :                uuid.UUID   = Field(default_factory=uuid.uuid4, primary_key=True)
    username:           str         = Field(index=True, unique=True)
    role:               str         = Field()
