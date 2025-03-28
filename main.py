from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from schema.schemas import Address_schema
from database.models import Base, drop_table, create_table
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Создать таблицы при запуске приложения
    await create_table()
    yield
    # Удаляем таблицы при выключении приложения
    await drop_table()

app = FastAPI(lifespan=lifespan)

@app.post('/address')
async def get_info_tron(user_address: Address_schema = Depends()):
    return {'message': user_address}



if __name__ == '__main__':
    uvicorn.run(app=app)