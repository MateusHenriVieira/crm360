from fastapi import APIRouter, Depends, HTTPException
from backend.app.models.lead import Lead
from backend.app.api.api_requirements import get_session_db, verify_token
from sqlalchemy.orm import Query, Session
from sqlalchemy import func
from typing import Optional, List
from backend.app.models.response_schemas import ResponseLead
from backend.app.models.user import User
from backend.app.models.request_schemas import SpecialtySchema
from backend.app.models.speciality import Specialty



lead_router = APIRouter(prefix="/api/leads", tags=["leads"])



@lead_router.get("", response_model=List[ResponseLead])
async def get_leads(skip: int = 0, limit: int = 100, speciality_id: Optional[int] = None, status: Optional[str] = None, session: Session = Depends(get_session_db), user_req: User = Depends(verify_token)):
    """Buscar leads com filtros"""
    query = session.query(Lead)
    
    if speciality_id:
        query = query.filter(Lead.speciality_id == speciality_id)
    if status:
        query = query.filter(Lead.status == status)
    
    leads = query.offset(skip).limit(limit).all()
    return leads



@lead_router.get("/by-specialty/{specialty}", response_model=List[ResponseLead])
async def get_leads_by_especiality(speciality: int, skip: int = 0, limit: int = 100, session: Session = Depends(get_session_db), user_req: User = Depends(verify_token)):
    query = session.query(Lead)
    leads = query.filter(Lead.speciality_id == speciality).offset(skip).limit(limit).all()
    return leads





@lead_router.post("/internal/create-speciality")
async def create_speciality(spec_data: SpecialtySchema, session: Session = Depends(get_session_db), user_req: User = Depends(verify_token)):
    if user_req.super_admin == False:
        raise HTTPException(status_code=401, detail=f"user {user_req.name} não está autorizado a criar novas especialidades")
    new_speciality = Specialty(spec_data.name, spec_data.description)
    flag_spec = session.query(Specialty).filter(Specialty.name == spec_data.name).first()
    if flag_spec:
        raise HTTPException(status_code=409, detail="impossivel criar especialidades com mesmo nome")
    session.add(new_speciality)
    session.commit()
    return {
        "OBS": f"Especialidade {new_speciality.name} criada!"
    }



@lead_router.get("/funnel-stages")
async def get_funnel(db: Session = Depends(get_session_db)):
    results = db.query(Lead.status, func.count(Lead.id).label("count")).group_by(Lead.status).all()

    funnel = [{"stage": status, "count": count} for status, count in results]
    return funnel
    



