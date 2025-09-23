from fastapi import FastAPI
from backend.app.api.auth import auth_router
from contextlib import asynccontextmanager
from backend.app.security.environment_variables import ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME
from sqlalchemy.orm import sessionmaker
from backend.app.models.user import User
from backend.app.security.password_hash import encrypter
from backend.app.models.db import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        conn = sessionmaker(bind=db)
        session = conn()
        admin_user = session.query(User).filter(User.name == ADMIN_NAME).first()
        if not admin_user:
            pass_hashed = encrypter.hash(ADMIN_PASSWORD)
            admin_account = User(ADMIN_NAME, ADMIN_EMAIL, pass_hashed, admin=True)
            session.add(admin_account)
            session.commit()
    finally:
        session.close()
    yield

app = FastAPI(lifespan=lifespan)


app.include_router(auth_router)

# evitar adicionar codigo a este modulo