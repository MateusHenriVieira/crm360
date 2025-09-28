#rotas

from fastapi import Apirouter, depends, httpexception
from sqlalchemy.orm import session
from app.core.confg import sessionlocal
from app.models.appointment import appointment
from app.schemas.appointment import appointmentcreate, appointmentout

router = Apirouter()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/", response_model=appointmentout)
def criar_appointment(app: appointmentcreate, db: session = depends(get_db)):
    novo = appointment(**app.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[appointment])
def listar_appointments(db: session = depends(get_db)):
    return db.query(appointment).all()