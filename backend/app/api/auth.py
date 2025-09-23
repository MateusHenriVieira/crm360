from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.api_requirements import get_session_db, make_token, verify_token
from backend.app.models.request_schemas import NewAccountSchema, LoginSchema
from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.security.password_hash import encrypter
from fastapi.security import OAuth2PasswordRequestForm


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


@auth_router.post("/login")
async def login(user_data = Depends(OAuth2PasswordRequestForm), session: Session = Depends(get_session_db)):
    ptr_user = session.query(User).filter(User.email == user_data.username).first()
    if not ptr_user:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    flag_password = encrypter.verify(user_data.password, ptr_user.password)
    if not flag_password:
        raise HTTPException(status_code=401, detail="credenciais invalidas")
    access_token = make_token(ptr_user)
    return{
        "access_token": access_token,
        "token-type": "Bearer"
    }
    
    

@auth_router.post("/login-teste") # OBS: Para tester de rotas protegidas. Use requests
async def login(user_data: LoginSchema, session: Session = Depends(get_session_db)):
    ptr_user = session.query(User).filter(User.email == user_data.email).first()
    if not ptr_user:
        raise HTTPException(status_code=404, detail="usuario não encontrado")
    flag_password = encrypter.verify(user_data.password, ptr_user.password)
    if not flag_password:
        raise HTTPException(status_code=401, detail="credenciais invalidas")
    access_token = make_token(ptr_user)
    return{
        "access_token": access_token,
        "token-type": "Bearer"
    }
