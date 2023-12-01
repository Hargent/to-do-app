import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from dotenv import load_dotenv
load_dotenv()



DATABASE_URL = os.getenv('DATABASE_URL')
# engine = create_engine(
#     SQLALCHEMY_DB_URL,
# #     pool_pre_ping= True,
#  )
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    # This function creates the tables
    Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()