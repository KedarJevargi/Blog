from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Annotated, List


class BlogOut(BaseModel):
    title:str
    body:str
    class Config:
        orm_mode = True


class AddUser(BaseModel):
   
    name: Annotated[str, Field(..., min_length=1, max_length=20, description="User name")]
    email: EmailStr
    password: Annotated[str, Field(..., description="User password")]

    @field_validator("name")
    @classmethod
    def name_cap(cls, value: str) -> str:
        return value.capitalize()
    
class UserOut(BaseModel):
    name:str
    email:str
    blogs:List[BlogOut]
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str



class TokenSchema(BaseModel):
    access_token: str
    token_type: str
