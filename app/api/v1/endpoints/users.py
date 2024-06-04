from fastapi import APIRouter, HTTPException
from app.schemas.user import User, UserCreate
from app.services.user_service import UserService

router = APIRouter()

@router.get("/", response_model=list[User])
async def read_users():
    return await UserService.get_users()

@router.post("/", response_model=User)
async def create_user(user: UserCreate):
    return await UserService.create_user(user)
