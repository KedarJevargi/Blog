import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from dotenv import load_dotenv
import logging
from models import Base  # SQLAlchemy models
from database import engine # DB connection setup
from routes import user, blog, home, login

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS settings (customize origins for your frontend)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optionally add session middleware for secure cookies
# app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET", "change_this_secret"))

# Automatically create all tables based on SQLAlchemy models
Base.metadata.create_all(bind=engine)

app.include_router(home.router)
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(login.router)

logger.info("Application startup complete.")






