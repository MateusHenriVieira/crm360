from fastapi import APIRouter, Depends
from backend.app.models.lead import Lead
from backend.app.api.api_requirements import get_session_db, verify_token
from sqlalchemy.orm import Query, Session
from typing import Optional, List
from backend.app.models.response_schemas import ResponseLead



lead_router = APIRouter(prefix="/api/leads", tags=["leads"])



@lead_router.get("/", response_model=List[ResponseLead])
async def get_leads(skip: int = 0, limit: int = 100, specialty_id: Optional[int] = None, status: Optional[str] = None, session: Session = Depends(get_session_db)):
    """Buscar leads com filtros"""
    query = session.query(Lead)
    
    if specialty_id:
        query = query.filter(Lead.specialty_id == specialty_id)
    if status:
        query = query.filter(Lead.status == status)
    
    leads = query.offset(skip).limit(limit).all()
    return leads



@lead_router.get("/by-specialty/{specialty}", response_model=List[ResponseLead])
async def get_by_especiality(specialty: int, skip: int = 0, limit: int = 100, session: Session = Depends(get_session_db)):
    query = session.query(Lead)
    leads = query.filter(Lead.specialty_id == specialty).offset(skip).limit(limit).all()
    return leads
