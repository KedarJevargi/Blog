from fastapi import APIRouter, Depends
from schema.blogpost import BlogPost, BlogUpdate, BlogOut  # Blog-related schemas
from schema.users import UserOut  # User creation schema
from sqlalchemy.orm import Session
from database import  get_db  # DB connection setup
from crud import *  # type: ignore # CRUD operations
from typing import List  # For response type annotations

router = APIRouter(
    tags=["Blogs"]
)


# Get all blogs - returns a list of blog posts
@router.get("/blog", response_model=List[BlogOut])
def get_all(db: Session = Depends(get_db)):
    return get_all_blog(db)

@router.get("/user/{id}", response_model=UserOut)
def u_get_by_id(id: int, db: Session = Depends(get_db)):
    return u_get_id(id, db)

@router.get("/blog/{id}", response_model=BlogOut)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return get_blog_and_creator_by_id(id, db)

# Create a new blog post
@router.post("/blog", status_code=201)
def create(data: BlogPost, db: Session = Depends(get_db)):
    return create_blog(data, db,4)

# Delete a blog post by ID
@router.delete("/blog/{id}")
def del_blog(id: int, db: Session = Depends(get_db)):
    return delete_id(id, db)

# Update an existing blog post by ID (partial update supported)
@router.put("/blog/{id}",)
def update_blog(id: int, data: BlogUpdate, db: Session = Depends(get_db)):
    return update_id(id, data, db)
