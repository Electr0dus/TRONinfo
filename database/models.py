from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine

engine = create_engine('sqlite:///wallet.db')

class Base(DeclarativeBase): pass


class Address_model(Base):
    __tablename__ = 'request_tron'
    
    id = Column(Integer, primary_key=True, index=True)
    address_name = Column(String)
    
    
