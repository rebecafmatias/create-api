from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///example.db")

Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_db_session():

    print("Creating a new database session")
    Base.metadata.create_all(bind=engine)
