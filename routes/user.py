from fastapi import APIRouter, Depends
from schema.users import UserOut, AddUser
from sqlalchemy.orm import Session
from database import get_db
from crud import u_get_all_blog, create_user
from typing import List
from routes.auth import get_current_user  # import auth dependency
import models

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=List[UserOut])
def u_get_all(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # Protect this route
):
    return u_get_all_blog(db)

@router.post("/user", status_code=201)
def add_user(
    user: AddUser,
    db: Session = Depends(get_db)
):
    return create_user(user, db)
