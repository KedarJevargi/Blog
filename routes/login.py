from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from schema.users import UserLogin, TokenSchema
from database import get_db
from routes.JWTtoken import create_access_token
import models

router = APIRouter(tags=["Login"])
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/login", response_model=TokenSchema)
def user_login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == data.username).first()
    
    if not user or not pwd_context.verify(data.password, user.password): # type: ignore
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = create_access_token(data={"sub": user.email})
    return TokenSchema(access_token=token, token_type="bearer")
