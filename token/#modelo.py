#modelo

from sqlalchemy import column, integer, string
from app.core.config import Base

class user(Base):
    _tablename_ = "users"
    
    id = column(integer, primary_key=True, index=True)
    nome = column(string, nullable=False)
    email = column(string, unique=True, index=True, nullable=False)
    senha = column(string, nullable=False)