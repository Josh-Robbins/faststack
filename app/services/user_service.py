from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

class UserService:
    @staticmethod
    async def get_users(db: AsyncSession):
        result = await db.execute(select(User))
        return result.scalars().all()

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate):
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
