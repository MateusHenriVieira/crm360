from fastapi import FastAPI
from backend.app.api.auth import auth_router
from backend.app.security.on_init import OnAPI__Init
from backend.app.api.routers.leads import lead_router
from backend.app.api.testes import teste_router


app = FastAPI(lifespan=OnAPI__Init)


app.include_router(auth_router)
app.include_router(lead_router)
app.include_router(teste_router)

# evitar adicionar codigo a este modulo