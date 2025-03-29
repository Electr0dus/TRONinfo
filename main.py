from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from schema.schemas import AddressResponse, AddressCreate
from database.models import drop_table, create_table, add_address
from database.models import AsyncSessionLocal
from loguru import logger
import uvicorn
from typing import AsyncGenerator


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Создали таблицу")
    await create_table()
    yield
    logger.info("Удалили таблицу")
    await drop_table()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


app = FastAPI(lifespan=lifespan)

@app.post('/address')
async def get_info_tron(user_address: AddressCreate = Depends(), db_session: AsyncSession = Depends(get_db)):
    logger.info("Добавили данные запроса в БД")
    user = await add_address(session=db_session, user=user_address)
    return {'user_id': user.id, 'user_address': user.address_name}



if __name__ == '__main__':
    uvicorn.run(app=app)