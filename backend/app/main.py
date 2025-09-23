from fastapi import FastAPI
from backend.app.api.auth import auth_router

app = FastAPI()


app.include_router(auth_router)

# evitar adicionar codigo a este modulo