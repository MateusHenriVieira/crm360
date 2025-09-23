from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ResponseLead(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    specialty_id: int
    status: str
    score: float
    source: str
    created_at: datetime
    updated_at: datetime
    avatar: Optional[bytes]
    class Config:
        from_attributes = True
        orm_mode = True
