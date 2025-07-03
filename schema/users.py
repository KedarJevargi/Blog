from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Annotated, List


class AddUser(BaseModel):
    """Schema for creating a new user."""
    name: Annotated[str, Field(..., min_length=1, max_length=20, description="User name")]
    email: EmailStr
    password: Annotated[str, Field(..., description="User password")]

    @field_validator("name")
    @classmethod
    def name_cap(cls, value: str) -> str:
        return value.capitalize()

class BlogOut(BaseModel):
    """Schema for outputting a blog post (for user relation)."""
    title: str
    body: str
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    """Schema for outputting a user with their blogs."""
    name: str
    email: str
    blogs: List[BlogOut]
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    """Schema for user login."""
    email: EmailStr
    password: str

class TokenSchema(BaseModel):
    """Schema for JWT token response."""
    access_token: str
    token_type: str
