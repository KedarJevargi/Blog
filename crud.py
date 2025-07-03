from sqlalchemy.orm import Session
from models import Blog,User
from schema.blogpost import BlogPost, BlogUpdate
from schema.users import AddUser
import models
from passlib.context import CryptContext
from fastapi import HTTPException, status


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_blog(data: BlogPost, db: Session, id:int):
    new_blog = Blog(title=data.title, body=data.body, user_id=id)
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


def get_blog_and_creator_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    return blog  # FastAPI will auto-serialize using BlogOut


from fastapi import HTTPException, status

def delete_id(id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)  # FIXED: blog_id → id
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
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)  # FIXED: blog_id → id
    blog = blog_query.first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found"
        )

    update_data = data.model_dump(exclude_unset=True)  # Pydantic v2
    blog_query.update(update_data, synchronize_session=False)  # type: ignore
    db.commit()

    return {"message": f"Blog with id {id} updated successfully"}



def create_user(data:AddUser, db: Session):
    hashedPassword=pwd_context.hash(data.password)
    new_user = User(name=data.name, email=data.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def u_get_all_blog(db: Session):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No blogs available"
        )
    return users

def u_get_id(id:int, db:Session):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {id} not found"
        )
    return user
    


    



