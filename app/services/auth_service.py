from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import RegisterRequest
from app.core.security import hash_password, verify_password, create_access_token

def register_user(db: Session, data: RegisterRequest):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        return None
    user = User(
        email=data.email,
        hashed_password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, data):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        return None
    if not verify_password(data.password, user.hashed_password):
        return None
    token = create_access_token({"sub": str(user.id)})
    return token