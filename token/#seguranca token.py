#seguranca token
# app/core/api_requirements.py
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
import os

secret_key = os.getenv("secret_key", "chave_de segurança")
Algorithm = "hs256"
access_token_expire_hours = 24

pwp_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwp_context.hash(password)

def verify_password(password: str, hasheh: str) -> bool:
    return pwp_context.verify(password, hasheh)

def create_token(user_id: int):
    expire = datetime.utcnow() + timedelta(hours=acess_token_expire_hours)
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, secret_key, algorithm=Algorithm)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[Algorithm])
        return int(payload.get("sub"))
    except JWTError:
        return None