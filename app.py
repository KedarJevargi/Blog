from fastapi import Depends, FastAPI,Response
from schema.blogpost import BlogPost, BlogUpdate
from sqlalchemy.orm import Session
from models import Base
from database import SessionLocal, engine
from models import Blog
from crud import *

Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message":"Welcome to home page"}

@app.get("/blogs")
def get_all(db: Session = Depends(get_db)):
    return get_all_blog(db)

@app.get("/blog/{id}")
def get_by_id(id:int,db: Session = Depends(get_db)):
    return get_id(id,db)

@app.post("/blog",status_code=201)
def create(data:BlogPost, db: Session = Depends(get_db)):
    return create_blog(data,db)


@app.delete("/blog/{id}")
def del_blog(id:int,db: Session = Depends(get_db)):
    return delete_id(id,db)


@app.put("/blog/{id}")
def update_blog(id: int, data: BlogUpdate, db: Session = Depends(get_db)):
    return update_id(id, data, db)






    
    
    
