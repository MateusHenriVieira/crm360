from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from backend.app.models.speciality import Specialty



class AppointmentModel(BaseModel):
    id: int
    lead_id: int
    speciality_id: int
    scheduled_date: datetime
    status: str
    notes: Optional[str] = None
    created_at: datetime
class SpecialityModel(BaseModel):
    name: str
class ResponseLead(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    speciality_id: int
    speciality: SpecialityModel
    status: str
    score: float
    source: str
    created_at: datetime
    updated_at: datetime
    avatar: Optional[bytes]
    appointments: list[AppointmentModel]
    class Config:
        from_attributes = True
