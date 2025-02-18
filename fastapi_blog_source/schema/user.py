from pydantic import BaseModel, Field, validator
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status

#properties required during user creation
# Request Body / payload / schema
class UserCreate(BaseModel):
    email : str
    password : str = Field(..., min_length=4)

    def __init__(self, **data):
        super().__init__(**data)

        if self.email:
            try:
                emailinfo = validate_email(self.email, check_deliverability=False)
                self.email = emailinfo.normalized
            except EmailNotValidError as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Not a valid email!"
                )


# Response Body / payload / schema
class UserView(BaseModel):
    id: int
    email : str
    is_active : bool
   
    class Config(): #tells pydantic to convert even non dict obj to json
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class UserProfileView(BaseModel):
    id: int
    email : str
    is_active : bool
    image_url : str
    
    @validator('image_url')
    def add_static_prefix(cls, v):
    # Add '/static/' to the filename if not already present
        return f"/static/{v}"
    
    class Config(): #tells pydantic to convert even non dict obj to json
        orm_mode = True