from pydantic import BaseModel
from typing import Optional
from datetime import datetime



class NewAccountSchema(BaseModel):
    name: str
    email: str
    password: str
    class Config:
        from_attributes = True
class LoginSchema(BaseModel):
    email: str
    password: str
    class Config:
        from_attributes = True



class LeadTeste(BaseModel):
    name: str
    email: str
    phone: Optional[str]
    specialty_id: int
    status: str
    score: float
    source: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    avatar: Optional[bytes]
    class Config:
        from_attributes = True
