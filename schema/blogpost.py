from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated, Optional
from schema.users import UserOut

class BlogPost(BaseModel):
    """Schema for creating a blog post."""
    title: Annotated[str, Field(..., max_length=20, description="Title of the blog")]
    body: Annotated[str, Field(..., max_length=1000, description="Body of the blog")]

class BlogUpdate(BaseModel):
    """Schema for updating a blog post (partial update supported)."""
    title: Optional[str] = None
    body: Optional[str] = None

class BlogOut(BaseModel):
    """Schema for outputting a blog post with creator info."""
    title: Annotated[str, Field(..., max_length=20, description="Title of the blog")]
    body: Annotated[str, Field(..., max_length=1000, description="Body of the blog")]
    creator: UserOut

    model_config = ConfigDict(from_attributes=True)
