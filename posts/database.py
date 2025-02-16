from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postresql://postgres:mysimplelife@localhost/fastapi"

engine = create_engine(url=SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()