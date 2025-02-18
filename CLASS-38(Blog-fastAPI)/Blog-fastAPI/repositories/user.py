from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Optional
from db.models.user import User
from fastapi import HTTPException
from utils.password_manager import PasswordManager
from fastapi.security import OAuth2PasswordBearer
from db.session import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=" /users/token")

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()
    
    def create_user(self, email: str, password: str, is_active: bool = True, is_superuser: bool = False) -> User:
        _hashed_password = PasswordManager.get_password_hash(password=password)
        
        db_user = User(email=email, password=_hashed_password, is_active=is_active, is_superuser=is_superuser)
        
        self.db.add(db_user)
        try:
            self.db.commit()
            self.db.refresh(db_user)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Email already registered")
        return db_user
    
    def get_user_by_id(self, id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == id, User.is_active==True).first()

    def get_user_for_token(self, email: str, passowrd: str) -> Optional[User]:
        user = self.get_user_by_email(email=email)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid Credentials")
        is_password_matched = PasswordManager.verify_password(passowrd, user.password)
        if not is_password_matched:
            raise HTTPException(status_code=401, detail="Invalid Credentials")
        
        return user