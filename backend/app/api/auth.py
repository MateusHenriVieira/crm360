from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.api_requirements import get_session_db
from backend.app.models.request_schemas import NewAccountSchema
from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.security.password_hash import encrypter


auth_router = APIRouter(prefix="/auth", tags= ["auth"])

@auth_router.post("/create-user")
async def create_user_account(user_data: NewAccountSchema, session: Session = Depends(get_session_db)):
    flag_user: bool = bool(session.query(User).filter(User.email == user_data.email).first())
    if flag_user:
        raise HTTPException(status_code=401, detail="email já existe")
    

    password = encrypter.hash(user_data.password)
    new_user = User(user_data.name, user_data.email, password)
    session.add(new_user)
    session.commit()
    return {
        "Message": f"Usuário {user_data.name} cadastrado com sucesso"
    }



