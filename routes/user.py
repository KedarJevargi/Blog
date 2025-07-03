from fastapi import APIRouter, Depends
from schema.users import UserOut, AddUser
from sqlalchemy.orm import Session
from database import get_db
from crud import u_get_all_blog, create_user
from typing import List

router = APIRouter(
    tags=["Users"]
)



@router.get("/users", response_model=List[UserOut])
def u_get_all(db: Session = Depends(get_db)):
    return u_get_all_blog(db)

# Route to create a new user
@router.post("/user",status_code=201)
def add_user(user: AddUser, db: Session = Depends(get_db)):
    return create_user(user, db)