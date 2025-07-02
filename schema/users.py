from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Annotated
from typing import Optional

class AddUser(BaseModel):
   
    name: Annotated[str, Field(..., min_length=1, max_length=20, description="User name")]
    email: EmailStr
    password: Annotated[str, Field(..., description="User password")]

    @field_validator("name")
    @classmethod
    def name_cap(cls, value: str) -> str:
        return value.capitalize()
    
class UserOut(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None

