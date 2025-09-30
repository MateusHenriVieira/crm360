from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from backend.app.models.db import db
from backend.app.models.user import User
from backend.app.security.environment_variables import ADMIN_PASSWORD, ADMIN_NAME, ADMIN_EMAIL
from backend.app.security.password_hash import encrypter










@asynccontextmanager
async def OnAPI__Init(app: FastAPI):
    print("Running Init API")
    try:
        conn = sessionmaker(bind=db)
        session = conn()
        admin_user = session.query(User).filter(User.name == ADMIN_NAME).first()
        if not admin_user:
            pass_hashed = encrypter.hash(ADMIN_PASSWORD)
            admin_account = User(ADMIN_NAME, ADMIN_EMAIL, pass_hashed, admin=True, super_admin=True)
            session.add(admin_account)
            session.commit()
    finally:
        session.close()
    yield