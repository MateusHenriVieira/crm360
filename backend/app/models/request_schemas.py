from pydantic import BaseModel
from typing import Optional



class NewAccountSchema(BaseModel):
    name: str
    email: str
    password: str
    class Config:
        from_attributes = True
class LoginSchema(BaseModel):
    email: str
    password: str
    class Config:
        from_attributes = True
