from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from repositories.user import UserRepository
from schema.user import UserCreate, UserView

router = APIRouter()


@router.post("", response_model=UserView)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
): # Depends: setting up prerequsities for API endpoint, setting it up is called dependency injection
    
    user_repo = UserRepository(db=db)
    existing_user = user_repo.get_user_by_email(email=payload.email)

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already exists!")

    new_user = user_repo.create_user(email=payload.email, password=payload.password)

    # return UserView(id=new_user.id, email=new_user.email, is_active=new_user.is_active)
    return new_user