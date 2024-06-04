from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models.item import Item
from app.schemas.item import ItemCreate

class ItemService:
    @staticmethod
    async def get_items(db: AsyncSession):
        result = await db.execute(select(Item))
        return result.scalars().all()

    @staticmethod
    async def create_item(db: AsyncSession, item: ItemCreate):
        db_item = Item(**item.dict())
        db.add(db_item)
        await db.commit()
        await db.refresh(db_item)
        return db_item
