from sqlalchemy import Column, Integer, String
from database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(20))
    body=Column(String(1000))




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)  # ✅ FIXED: length increased
    password = Column(String(255), nullable=False)
