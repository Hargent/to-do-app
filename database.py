from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Create sqlite engine instance
engine = create_engine("sqlite:///todo.db")

# Create a declarative meta instance
Base = declarative_base()

# Create SessionLocal class from sessionmaker factory
sessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
