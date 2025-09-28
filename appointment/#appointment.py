#appointment

from sqlalchemy import column, integer, foreignkey, datatime, string
from sqlalchemy.org import relationship
from app.core.config import base

class appointment(base):
    _tablename_="appointments"
    
    id = column(integer, primary_key=True, index=True)
    lead_id = column(integer, foreignkey("leads.id"))
    especialidade_id = column(integer, foreignkey("especialidade.id"))
    data_hora = column(datatime, nullable=False)
    status = column(string, default="pendente")
    
    lead = relationship("lead", back_populates="appointments")
    especialidade = relationship("especialidade", back_populates="appointments")



#os codigos aqui corno

#aqui vai pro lead.py

appointments = relationship("Appointment", back_populates="lead")

#aqui vai no speciality.py

appointments = relationship("Appointment", back_populates="especialidade")