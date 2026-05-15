from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base




DATABASE_URL = "sqlite:///./leetcode.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

from models import SubmissionModel
Base.metadata.create_all(bind=engine)