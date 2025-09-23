from fastapi import Depends, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from backend.app.models.db import db
from jose import jwt, JWTError
from backend.app.models.user import User
from datetime import datetime, timedelta, timezone
from backend.app.security.environment_variables import SECRET_KEY, ALGORITHM
from backend.app.security.token import oauth2_schema

def get_session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()




def make_token(user: User, expire: timedelta = timedelta(hours=24)):
    expiration = datetime.now(timezone.utc) + expire

    payload = {
        "sub": str(user.id),
        "exp": expiration
    }

    encoded_payload = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return encoded_payload


def verify_token(token = Depends(oauth2_schema), session: Session = Depends(get_session_db)):
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=401, detail="rota não autorizada")
    user_id = decoded_payload.get("sub")
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="usuario não listado no db")
    return user