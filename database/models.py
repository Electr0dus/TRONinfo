from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine('sqlite+aiosqlite:///wallet.db')
meta = MetaData()

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(meta.create_all)

async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)

class Base(DeclarativeBase): pass


class Address_model(Base):
    __tablename__ = 'request_tron'
    
    id = Column(Integer, primary_key=True, index=True)
    address_name = Column(String)
    
    
