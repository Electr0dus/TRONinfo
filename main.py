from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from schema.schemas import AddressResponse, AddressCreate, AddressUserTRX
from database.models import drop_table, create_table, add_address, get_address
from database.models import AsyncSessionLocal
from loguru import logger
import uvicorn
from typing import AsyncGenerator

from TronConn import get_info_TRX

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
async def get_info_tron(user_address: AddressUserTRX = Depends(), db_session: AsyncSession = Depends(get_db)):
    logger.info("Добавили данные запроса в БД")
    data_tron = get_info_TRX(user_address.address)
    data_tron.update({'address_name': user_address.address})
    print(data_tron)
    await add_address(session=db_session, user=data_tron)
    return {'data_tron': data_tron}


@app.get('/address')
async def get_all_data_tron(db_session: AsyncSession = Depends(get_db)):
    logger.info("Получить данные из БД")
    data_tron = await get_address(session=db_session)
    return {"data": data_tron}



if __name__ == '__main__':
    uvicorn.run(app=app)