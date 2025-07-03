from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from schema.users import UserLogin, TokenSchema
from database import get_db
from routes.JWTtoken import create_access_token
import models

router = APIRouter(tags=["Login"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from fastapi.security import OAuth2PasswordRequestForm
from schema.users import TokenSchema

@router.post("/login", response_model=TokenSchema)
def user_login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.username).first()  # Note: `data.username`
    
    if not user or not pwd_context.verify(data.password, user.password): # type: ignore
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(data={"sub": user.email})
    return TokenSchema(access_token=token, token_type="bearer")


