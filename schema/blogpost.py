from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional

class BlogPost(BaseModel):
    title: Annotated[str, Field(..., max_length=20, description="Title of the blog")]
    body: Annotated[str, Field(..., max_length=1000, description="Body of the blog")]

class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None

class UserOut(BaseModel):
    name: str
    email: EmailStr

    class Config:
        orm_mode = True

class BlogOut(BaseModel):
    title: Annotated[str, Field(..., max_length=20, description="Title of the blog")]
    body: Annotated[str, Field(..., max_length=1000, description="Body of the blog")]
    creator: UserOut  # This must match the SQLAlchemy relationship name

    class Config:
        orm_mode = True
