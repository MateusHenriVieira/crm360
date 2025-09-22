from pydantic import BaseModel
from typing import Optional



class NewAccountSchema(BaseModel):
    name: str
    email: str
    password: str