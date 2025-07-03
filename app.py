from fastapi import FastAPI
from models import Base  # SQLAlchemy models
from database import engine # DB connection setup
from routes import user, blog, home, login

app = FastAPI()

# Automatically create all tables based on SQLAlchemy models
Base.metadata.create_all(bind=engine)

app.include_router(home.router)
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(login.router)


# Initialize FastAPI app


# Dependency for providing a DB session per request




