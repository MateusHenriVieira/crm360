#schemas

from pydantic import basemodel
from datetime import datetime

class appointmentbase(basemodel):
    lead_id: int
    especialidade_id: int
    data_hora: datetime
    
class appointmentcreate(appointmentbase):
    pass

class appointmentout(appointmentbase):
    id: int
    status: str
    
class config:
    orm_mode = True