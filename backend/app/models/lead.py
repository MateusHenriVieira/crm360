from backend.app.models.db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, LargeBinary
from datetime import datetime
from fastapi import Response


class Lead(Base):
    __tablename__ = "leads"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=False)
    specialty_id = Column(Integer)
    status = Column(String, default="novo")  # novo, qualificado, agendado, convertido, perdido
    score = Column(Float, default=0.0)  # Lead scoring IA
    source = Column(String)  # whatsapp, instagram, facebook, google, email
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    avatar = Column("img", LargeBinary, nullable=True, default=None)

    def __init__(this, name, email, specialty_id, status, score, source, avatar=None, phone=None):
        this.name = name
        this.email = email
        this.phone = phone
        this.specialty_id = specialty_id
        this.status = status
        this.score = score
        this.source = source
        this.avatar = avatar
        
    def get_img_response(this, media_type: str = "image/png"):
        if not this.avatar:
            return Response(content=b"", media_type=media_type, status_code=404)
        
        return Response(content=this.avatar, media_type=media_type)