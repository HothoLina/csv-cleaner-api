from fastapi import APIRouter, UploadFile, File
from pathlib import Path
import shutil

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "CSV Cleaner API is running."
    }
    
    
@router.post("/upload")
def upload_csv(file: UploadFile = File(...)):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)

    file_path = upload_dir / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully!",
        "filename": file.filename
    }