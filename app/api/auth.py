from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = register_user(db, data)
    if not user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return {"message": "User registered successfully", "email": user.email}

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    token = login_user(db, data)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"access_token": token, "token_type": "bearer"}