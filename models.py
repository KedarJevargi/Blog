from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Blog(Base):
    __tablename__ = "blogs"

    blog_id = Column(Integer, primary_key=True, index=True)  # Primary key
    title = Column(String(20), nullable=False)
    body = Column(String(1000), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))  # Foreign key to User

    creator = relationship("User", back_populates="blogs")  # Many-to-One

class User(Base):
    __tablename__ = "users"

    User_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False) 
    password = Column(String(255), nullable=False)

    blogs = relationship("Blog", back_populates="creator")  # One-to-Many
