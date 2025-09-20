# leads.py

from sqlalchemy import Column, Integer, String
from app.core.config import base


class lead(base):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefone_celular = Column(String, unique=True, index=True)
    status = Column(String, default="novo")
