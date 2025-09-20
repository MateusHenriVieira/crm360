# rota mo main.py

from fastapi import FastAPI
from app.routers import leads


base.metadata.create_all(bind=engine)

app = FastAPI(title="crm", version="0.1.0")

app.include_router(leads.router, prefix="api/leads", tags=["leads"])


@app.get("/")
def raiz():
    return {"status da api": "api crm ok"}
