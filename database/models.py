from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from schema.schemas import AddressCreate

engine = create_async_engine('sqlite+aiosqlite:///wallet.db')
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session

async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

class Base(DeclarativeBase): pass


class Address_model(Base):
    __tablename__ = 'request_tron'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address_name = Column(String)
    

async def add_address(session: AsyncSessionLocal, user: AddressCreate):
    new_user = Address_model(**user.model_dump())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user
        
        
