from pydantic import BaseModel

class AddressCreate(BaseModel):
    address_name: str
    
class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True