from pydantic import BaseModel

class AddressUserTRX(BaseModel):
    address: str

class AddressCreate(BaseModel):
    Balance: str
    Bandwidth: int
    Energy: str
    address_name: str
    
class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True