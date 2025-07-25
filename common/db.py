from fastapi import Depends
from typing import Annotated

from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.exc import OperationalError

import os
import time

url = os.environ["DATABASE_URL"]
engine = create_engine(url)
SQLModel.metadata.create_all(engine)

def wait_for_db():
    retries = 5
    while retries:
        try:
            SQLModel.metadata.create_all(engine)
            return
        except OperationalError:
            retries -= 1
            time.sleep(5)
    raise Exception(f"Failed to connect to database. Retries : {retries}. URL : {url}.")

def get_session():
    with Session(engine) as session:
        yield session

# Database session dependency injection
SessionDep = Annotated[Session, Depends(get_session)]
