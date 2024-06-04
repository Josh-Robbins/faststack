from sqlalchemy import Column, Integer, String, Float
from app.db.base import Base

class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
