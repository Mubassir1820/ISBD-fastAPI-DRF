#main.py

from fastapi import Depends, FastAPI
from core.config import settings
from apis.base import api_router
from db.models.user import User
from repositories.user import UserRepository
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

app.mount("/static", StaticFiles(directory="uploads/images"), name="static")
app.include_router(api_router)


# List of allowed origins, you can add specific domains or '*' for all origins
origins = [
    "http://localhost:3000", # Frontend during development
    "https://your-frontend-domain.com", # Production frontend
]

# Adding CORSMiddleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # List of allowed origins
    allow_credentials=True, # Allow cookies and credentials to be sent
    allow_methods=["*"], # Allowed HTTP methods
    allow_headers=["*"], # Allowed headers
)


@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI"}


@app.get("/protected")
async def protected_route(current_user: User = Depends(UserRepository.get_current_user)):
    return {"message": f"Hello {current_user.email}, you are authorized!"}  
