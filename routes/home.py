from fastapi import APIRouter

router = APIRouter(
    tags=["Home"]
)


# Home route - simple health check or landing page
@router.get("/")
def home():
    return {"message": "Welcome to home page"}