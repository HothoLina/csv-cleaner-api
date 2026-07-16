from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="CSV Cleaner API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the CSV Cleaner API!"
    }