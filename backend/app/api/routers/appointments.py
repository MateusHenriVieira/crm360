from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.api_requirements import get_session_db, verify_token
from sqlalchemy.orm import Query, Session
from sqlalchemy import func
from typing import Optional, List
from backend.app.models.user import User
from backend.app.models.appointment import Appointment



appo_router = APIRouter(prefix="/appointments", tags=["apointments"])



@appo_router.get("")
async def get_appointments(lead_id, offset = 0, limit = 100, session: Session = Depends(get_session_db), speciality_id: Optional[int] = None):
    appo = session.query(Appointment)
    if lead_id:
        appo = appo.filter(Appointment.lead_id == lead_id)
    if speciality_id:
        appo = appo.filter(Appointment.speciality_id == speciality_id)

    appo = appo.offset(offset).limit(limit).all()
     
    return appo