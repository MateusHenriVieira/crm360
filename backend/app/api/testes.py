from backend.app.api.api_requirements import get_session_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.models.lead import Lead
from backend.app.models.request_schemas import LeadTeste

teste_router = APIRouter(prefix="/teste", tags=["teste"])



@teste_router.post("/create-fakelead")
async def create(lead_data:  LeadTeste, session : Session = Depends(get_session_db)):
    new_lead = Lead(lead_data.name, lead_data.email, lead_data.specialty_id, lead_data.status, lead_data.score, lead_data.source, lead_data.avatar, lead_data.phone)
    session.add(new_lead)
    session.commit()
    return {
        "message": "lead added"
    }




@teste_router.post("/delete-fakelead")
async def delete(lead_id: int, session : Session = Depends(get_session_db)):
    lead = session.query(Lead).filter(Lead.id == lead_id).first()
    session.delete(lead)
    session.commit()
