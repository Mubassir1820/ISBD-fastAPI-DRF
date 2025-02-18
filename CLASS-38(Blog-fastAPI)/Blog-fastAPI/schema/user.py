from pydantic import BaseModel, Field
from email_validator import validate_email, EmailNotValidError
from fastapi import HTTPException, status

# Prperties required for user creation
# Request body/ payload / schema
class UserCreate(BaseModel):
    email: str
    password: str = Field(... , min_length=4)

    def __init__(self, **data):
        super().__init__(**data)

        if self.email:
            try:
                emailinfo = validate_email(self.email, check_deliverability=False)
                self.email = emailinfo.normalized

            except EmailNotValidError as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not a valid email")

# Response Body / payload / schema
class UserView(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"