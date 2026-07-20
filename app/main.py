from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="CSV Cleaner API",
    version="1.0.0"
)

from app.core.handlers import (
    csv_exception_handler,
    unexpected_exception_handler,
)

from app.core.exceptions import CSVCleanerException

app.add_exception_handler(
    CSVCleanerException,
    csv_exception_handler,
)

app.add_exception_handler(
    Exception,
    unexpected_exception_handler,
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to the CSV Cleaner API!"
    }