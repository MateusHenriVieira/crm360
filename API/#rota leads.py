# rota leads.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.lead import LeadCreate, leadout
from app.models import Lead
from app.core.config import sessionLocal

router = APIRouter()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/leads/", response_model=leadout)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    novo_lead = Lead(**lead.dict())
    db.add(novo_lead)
    db.commit()
    db.refresh(novo_lead)
    return novo_lead


@router.get("/leads/", response_model=list[leadout])
def list_leads(db: Session = Depends(get_db)):
    return db.query(Lead).all()
