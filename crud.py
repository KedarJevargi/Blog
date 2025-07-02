from sqlalchemy.orm import Session
from models import Blog
from schema.blogpost import BlogPost, BlogUpdate
import models

from fastapi import HTTPException, status,Response

def create_blog(data: BlogPost, db: Session):
    new_blog = Blog(title=data.title, body=data.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_all_blog(db: Session):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No blogs available"
        )
    return blogs

def get_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )
    return blog

from fastapi import HTTPException, status

def delete_id(id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    blog_query.delete(synchronize_session=False)
    db.commit()

    return {"message": f"Blog with id {id} deleted successfully"}

    


def update_id(id: int, data: BlogUpdate, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    update_data = data.model_dump(exclude_unset=True)  # or .dict() if on Pydantic v1

    blog_query.update(update_data, synchronize_session=False) # type: ignore
    db.commit()

    return {"message": f"Blog with id {id} updated successfully"}


    



