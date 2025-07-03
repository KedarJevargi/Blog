"""
CRUD operations for Blog and User models.
"""
from sqlalchemy.orm import Session
from models import Blog, User
from schema.blogpost import BlogPost, BlogUpdate
from schema.users import AddUser
from passlib.context import CryptContext
from fastapi import HTTPException, status
from typing import List, Dict, Any

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Blog CRUD

def create_blog(data: BlogPost, db: Session, user_id: int) -> Blog:
    """Create a new blog post for a user."""
    new_blog = Blog(title=data.title, body=data.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all_blog(db: Session) -> List[Blog]:
    """Retrieve all blog posts."""
    blogs = db.query(Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No blogs available"
        )
    return blogs


def get_blog_and_creator_by_id(id: int, db: Session) -> Blog:
    """Retrieve a blog post and its creator by blog ID."""
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog


def delete_id(id: int, db: Session) -> Dict[str, Any]:
    """Delete a blog post by ID."""
    blog_query = db.query(Blog).filter(Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    blog_query.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Blog with id {id} deleted successfully"}


def update_id(id: int, data: BlogUpdate, db: Session) -> Dict[str, Any]:
    """Update a blog post by ID."""
    blog_query = db.query(Blog).filter(Blog.id == id)
    blog = blog_query.first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    update_data = data.model_dump(exclude_unset=True)
    # Map keys to actual columns
    for key, value in update_data.items():
        setattr(blog, key, value)
    db.commit()
    return {"message": f"Blog with id {id} updated successfully"}

# User CRUD

def create_user(data: AddUser, db: Session) -> User:
    """Create a new user with hashed password."""
    hashed_password = pwd_context.hash(data.password)
    new_user = User(name=data.name, email=data.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session) -> List[User]:
    """Retrieve all users."""
    users = db.query(User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No users available"
        )
    return users


def get_user_by_id(id: int, db: Session) -> User:
    """Retrieve a user by ID."""
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    return user







