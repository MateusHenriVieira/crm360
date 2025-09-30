from backend.app.models.db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, LargeBinary
from datetime import datetime, timezone, timedelta
from fastapi import Response
import enum
from sqlalchemy.orm import relationship


class LeadStatus(str, enum.Enum):
    NOVO = "novo"
    QUALIFICADO = "qualificado"
    AGENDADO = "agendado"
    CONVERTIDO = "convertido"
    PERDIDO = "perdido"





class Lead(Base):
    __tablename__ = "leads"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=False)
    speciality_id = Column(Integer, ForeignKey("specialties.id"))
    speciality = relationship("Specialty", back_populates="leads")
    appointments = relationship("Appointment", back_populates="lead")
    status = Column(String, default=LeadStatus.NOVO)  # novo, qualificado, agendado, convertido, perdido
    score = Column(Float, default=0.0)  # Lead scoring IA
    source = Column(String)  # whatsapp, instagram, facebook, google, email
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    avatar = Column("img", LargeBinary, nullable=True, default=None)



    lead_stages = ["novo", "qualificado", "agendado", "convertido", "perdido"]




    def __init__(this, name, email, speciality_id, status, score, source, avatar=None, phone=None):
        this.name = name
        this.email = email
        this.phone = phone
        this.speciality_id = speciality_id
        this.status = status
        this.score = score
        this.source = source
        this.avatar = avatar

    def update_time(this):
        utc_br = timezone(timedelta(hours=-3))
        this.updated_at = datetime.now(utc_br)
        return
    


    def advance_stage(this, next_stage: str):

        valid_stages = ["novo", "qualificado", "agendado", "convertido", "perdido"]

        if next_stage not in valid_stages:

            raise ValueError(f"Stage inválido: {next_stage}")
        
        this.status = next_stage

        this.updated_at = datetime.utcnow()

    def mark_lost(this):

        this.status = "perdido"

        this.updated_at = datetime.utcnow()

    def is_stage(this, stage_name: str) -> bool:
        return this.status == stage_name
    

