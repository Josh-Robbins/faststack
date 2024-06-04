from fastapi import APIRouter, HTTPException
from app.schemas.item import Item, ItemCreate
from app.services.item_service import ItemService

router = APIRouter()

@router.get("/", response_model=list[Item])
async def read_items():
    return await ItemService.get_items()

@router.post("/", response_model=Item)
async def create_item(item: ItemCreate):
    return await ItemService.create_item(item)
