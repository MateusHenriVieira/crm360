from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text
from backend.app.models.db import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    speciality_id = Column(Integer, ForeignKey("specialties.id"))
    scheduled_date = Column(DateTime, nullable=False)
    status = Column(String, default="agendado")  # agendado, confirmado, realizado, cancelado, falta
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    lead = relationship("Lead", back_populates="appointments")
    specialty = relationship("Specialty")


    def __init__(this, lead_id, speciality_id, scheduled_date, notes=""):
        this.lead_id = lead_id
        this.speciality_id = speciality_id
        this.scheduled_date = scheduled_date
        this.notes = notes


    def update_status(this, status):
        sts_array = ["agendado","confirmado","realizado","cancelado", "falta"]
        if status in sts_array:
            this.status = status
        else:
            raise ValueError("status inexistente")