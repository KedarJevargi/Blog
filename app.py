from fastapi import Depends, FastAPI, Response
from schema.blogpost import BlogPost, BlogUpdate, BlogOut  # Blog-related schemas
from schema.users import AddUser,UserOut  # User creation schema
from sqlalchemy.orm import Session
from models import Base, Blog  # SQLAlchemy models
from database import SessionLocal, engine  # DB connection setup
from crud import *  # type: ignore # CRUD operations
from typing import List  # For response type annotations


# Automatically create all tables based on SQLAlchemy models
Base.metadata.create_all(bind=engine)



# Initialize FastAPI app
app = FastAPI()

# Dependency for providing a DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home route - simple health check or landing page
@app.get("/")
def home():
    return {"message": "Welcome to home page"}

# Get all blogs - returns a list of blog posts
@app.get("/blogs", response_model=List[BlogOut])
def get_all(db: Session = Depends(get_db)):
    return get_all_blog(db)

@app.get("/users", response_model=List[UserOut])
def u_get_all(db: Session = Depends(get_db)):
    return u_get_all_blog(db)

# Route to create a new user
@app.post("/user",status_code=201)
def add_user(user: AddUser, db: Session = Depends(get_db)):
    return create_user(user, db)



# Get a specific blog by ID
@app.get("/blog/{id}", response_model=BlogOut)
def get_by_id(id: int, db: Session = Depends(get_db)):
    return get_id(id, db)

# Create a new blog post
@app.post("/blog", status_code=201)
def create(data: BlogPost, db: Session = Depends(get_db)):
    return create_blog(data, db)

# Delete a blog post by ID
@app.delete("/blog/{id}")
def del_blog(id: int, db: Session = Depends(get_db)):
    return delete_id(id, db)

# Update an existing blog post by ID (partial update supported)
@app.put("/blog/{id}")
def update_blog(id: int, data: BlogUpdate, db: Session = Depends(get_db)):
    return update_id(id, data, db)
