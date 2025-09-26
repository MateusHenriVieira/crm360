from backend.app.models.db import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship


class Specialty(Base):

    __tablename__ = "specialties"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(Text)
    color = Column(String, default="#64748b")
    leads = relationship("Lead", back_populates="speciality")

    def __init__(this, name, description):
        this.name = name
        this.description = description

    def set_color(this, color: str):
        this.color = color
        return