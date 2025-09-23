#RH

from fastapi import FastAPI
from app.routers import auth
from app.core.confg import base, engine

base.metade.create_all(bind=engine)

app = FastAPI(title="crm360 - api", version="1.0")

app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])