#rotas

from fastapi import apirouter, depends, httpexception, status
from sqlalchemy.org import sesssion
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.core.confg import sessionlocal
from app.core.security import hash_password, verify_password, create_token, verify_token
from app.models.user import user
from app.schemas.user import usercreate, userout, token

router = apirouter()
OAuth2_scheme = OAuth2PasswordBearer(tokenurl="/api/auth/login")

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()
        
#user
@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    novo_user = User(nome=user.nome, email=user.email, senha=hash_password(user.senha))
    db.add(novo_user)
    db.commit()
    db.refresh(novo_user)
    return novo_user

#login com gmail

@router.post("/login", response_model=Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form.username).first()
    if not user or not verify_password(form.password, user.senha):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    token = create_token(user.id)
    return {"access_token": token, "token_type": "bearer"}

#rota

@router.get("/me", response_model=UserOut)
def me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Token inválido ou expirado")
    user = db.query(User).filter(User.id == user_id).first()
    return user