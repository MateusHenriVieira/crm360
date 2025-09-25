from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from backend.app.models.speciality import Specialty




class SpecialtyModel(BaseModel):
    name: str
class ResponseLead(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    specialty_id: int
    speciality: SpecialtyModel
    status: str
    score: float
    source: str
    created_at: datetime
    updated_at: datetime
    avatar: Optional[bytes]
    class Config:
        from_attributes = True
