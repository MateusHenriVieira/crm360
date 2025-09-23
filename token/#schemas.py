#schemas

from pydantic import basemodel

class userbase(basemodel):
    nome: str
    email: str

class usercreate(userbase):
    senha: str
    
class userout(userbase):
    id: int
    class config:
        orm_mode = True
    
class token(basemodel):
    access_token: str
    token_type: str = "bearer"