import os
from uuid import uuid4
from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from db.models.user import User
from db.session import get_db
from repositories.user import UserRepository
from schema.user import Token, UserCreate, UserProfileView, UserView
from utils.const import UPLOAD_FOLDER
from utils.jwt_manager import create_access_token, create_refresh_token, verify_token

router = APIRouter()

@router.post("", response_model=UserView)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db),
):
    user_repo = UserRepository(db=db)
    existing_user = user_repo.get_user_by_email(email=payload.email)

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists!"
        )
    
    new_user = user_repo.create_user(email=payload.email, password=payload.password)
    
    # return UserView(id=new_user.id, email=new_user.email, is_active=new_user.is_active)
    return new_user


# Route for getting the token (login)
@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = UserRepository(db=db).get_user_for_token(
        email=form_data.username, password=form_data.password
    )
    token_subject = {"sub": str(user.id)}
    access_token = create_access_token(data=token_subject)
    refresh_token = create_refresh_token(data=token_subject)
    return {"access_token": access_token, "refresh_token": refresh_token}

@router.post("/refresh", response_model=Token)
async def refresh_access_token(refresh_token: str, db: Session = Depends(get_db)):
    payload = verify_token(refresh_token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    payload_subject = payload.get("sub")
    user = UserRepository(db=db).get_user_by_id(id=payload_subject)
    
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    token_subject = {"sub": str(user.id)}
    new_access_token = create_access_token(data=token_subject)
    new_refresh_token = create_refresh_token(data=token_subject)

    return {"access_token": new_access_token, "refresh_token": new_refresh_token}

@router.put("/upload_image")
async def upload_image(
    file: UploadFile = File(...),
    current_user: User = Depends(UserRepository.get_current_user),
    db: Session = Depends(get_db)
):
    # Ensure the file is an image (you can extend the validation if needed)
    if not file.content_type.startswith('image'):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image")
    
    # Todo: check image size also here (not more than 500kb)
    
    user_repo = UserRepository(db=db)

    # If the user already has an image, remove the old image
    old_image_path = current_user.image_url
    if old_image_path:
        user_repo.remove_previous_image(old_image_path)


    # Generate a unique filename for the new image
    unique_filename = f"{uuid4()}_{file.filename}"
    new_file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
    
    # Save the new image file to the server
    with open(new_file_path, "wb") as buffer:
        buffer.write(await file.read())

    user_repo.save_image_path_to_db(user=current_user, new_image_path=unique_filename)
    
    return {
        "success" : "Successfully uploaded image!",
        "path" : f"/static/{unique_filename}"
    }


@router.get("/profile", response_model=UserProfileView)
async def get_current_user(current_user: User = Depends(UserRepository.get_current_user)):
    return current_user