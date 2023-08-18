from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Generator


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print(f"Database URL is: {SQLALCHEMY_DATABASE_URL}")
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'
# # sqlite db cannot handle multiple threads
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})


SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)   # set of sessions; by creating an instance of it, we get an actual db session


def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()
