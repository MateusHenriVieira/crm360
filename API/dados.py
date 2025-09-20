from pydantic import BaseModel


class leadbase(BaseModel):
    nome: str
    email: str
    telefone_celular: str


class leadcreate(leadbase):
    pass


class leadout(leadbase):
    id: int
    status: str


class configuracoes:
    orm_mode = True
