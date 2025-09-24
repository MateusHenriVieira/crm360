from fastapi import APIRouter, Depends, HTTPException
from backend.app.api.api_requirements import get_session_db, make_token, verify_token
from backend.app.models.request_schemas import NewAccountSchema, LoginSchema
from sqlalchemy.orm import Session
from backend.app.models.user import User
from backend.app.security.password_hash import encrypter
from fastapi.security import OAuth2PasswordRequestForm


auth_router = APIRouter(prefix="/api", tags= ["api"])

@auth_router.post("/auth/create-user")
async def create_user_account(user_data: NewAccountSchema, session: Session = Depends(get_session_db), user_req: User = Depends(verify_token)):
    if user_req.admin == False:
        raise HTTPException(status_code=401, detail="apenas usuarios admin podem criar novas contas")
    flag_email: bool = bool(session.query(User).filter(User.email == user_data.email).first())
    flag_name: bool = bool(session.query(User).filter(User.name == user_data.name).first())
    if flag_name:
        raise HTTPException(status_code=409, detail="mome já existe")
    if flag_email:
        raise HTTPException(status_code=409, detail="email já existe")
    

    password = encrypter.hash(user_data.password)
    new_user = User(user_data.name, user_data.email, password)
    session.add(new_user)
    session.commit()
    return {
        "Message": f"Usuário {user_data.name} cadastrado com sucesso"
    }


@auth_router.post("/auth/login")
async def login(user_data = Depends(OAuth2PasswordRequestForm), session: Session = Depends(get_session_db)):
    print("running print func")
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
    
    

@auth_router.post("/auth/login-teste") # OBS: Para tester de rotas protegidas. Use requests
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
@auth_router.post("/auth/set-admin")
async def set_admin_account(user_id: int, adm: bool, session: Session = Depends(get_session_db), user_req: User = Depends(verify_token)):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="usuario nao encontrado")
    if user_req.id != 1 and user.admin == True:
        raise HTTPException(status_code=401, detail=f"usuario {user_req.name} não autorizado")
    if adm:
        user.admin = True
        session.commit()
        return{
            "warning": f"Usuario {user.name} agora é um administrador"
        }
    if not adm:
        user.admin = False
        session.commit()
        return{
            "warning": f"Usuario {user.name} não é mais um administrador"
        }
    

@auth_router.delete("/auth/delete-user")
async def delete_user(user_id: int, session: Session = Depends(get_session_db), user_req: User = Depends(verify_token)):
    if user_req.id != 1:
        raise HTTPException(status_code=401, detail=f"usuario {user_req.name} não autorizado")
    user = session.query(User).filter(User.id == user_id).first()
    session.delete(user)
    session.commit()
    return {
        "Warning": f"Usuario {user.name} deletado"
    }