from fastapi import FastAPI
from schema.blogpost import BlogPost
from models import Base
from database import SessionLocal, engine



Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def home():
    return {"message":"Welcome to home page"}


@app.post("/blog")
def create(data:BlogPost):
    return{"title":data.title,
            "body":data.body
            }
