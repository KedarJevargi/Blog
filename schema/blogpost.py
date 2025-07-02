from pydantic import BaseModel,Field
from typing import Annotated
from typing import Optional



class BlogPost(BaseModel):
    title: Annotated[str, Field(..., max_length=20, description="Title of the blog")]
    body: Annotated[str, Field(..., max_length=1000, description="Body of the blog")]



class BlogUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None