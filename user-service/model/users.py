from sqlmodel import Field, SQLModel

from enum import Enum

class UserRole(str, Enum):
    advertiser = "advertiser"
    client = "client"

class User(SQLModel, table=True):
	id : int | None = Field(default = None, primary_key=True)
    username: str = Field(index=True, unique=True)
    role: str = Field()
    hashed_password : str = Field()
    