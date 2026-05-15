from sqlalchemy import Column, Integer, String
from database import Base

class SubmissionModel(Base):

    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)

    leetcode_id = Column(Integer)

    language = Column(String)

    code = Column(String)