#ponto de entrada
from fastapi import FastAPI
app = FastAPI(title="crm", version="0.1.0")


@app.get("/")
def raiz():
    return {"status": "api do crm ok"}
