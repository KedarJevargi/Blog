from pydantic import BaseModel,Field
from typing import Annotated


class BlogPost(BaseModel):
    title: Annotated[str, Field(..., max_length=20, description="Title of the blog")]
    body: Annotated[str, Field(..., max_length=20, description="Body of the blog")]
