#main.py
from fastapi import FastAPI
from core.config import settings
from apis.base import api_router
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION)


app.include_router(api_router)


@app.get("/")
def hello_api():
    print(settings.DATABASE_URL)
    return {"msg":"Hello FastAPI"}
