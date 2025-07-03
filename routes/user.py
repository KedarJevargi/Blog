from fastapi import APIRouter, Depends
from schema.users import UserOut, AddUser
from sqlalchemy.orm import Session
from database import get_db
from crud import get_all_users, create_user  # updated import
from typing import List
from routes.auth import get_current_user  # import auth dependency
import models

router = APIRouter(tags=["Users"])

@router.get("/users", response_model=List[UserOut])
def u_get_all(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)  # Protect this route
):
    return get_all_users(db)  # updated function name

@router.post("/user", status_code=201)
def add_user(
    user: AddUser,
    db: Session = Depends(get_db)
):
    return create_user(user, db)
