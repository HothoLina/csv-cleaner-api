from app.services.cleaner import inspect_csv, remove_duplicates
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

    # Read the saved CSV file and return basic metadata
    try:
        csv_info = inspect_csv(file_path)
    except Exception as e:
        return {"message": "File uploaded but failed to read CSV", "error": str(e)}

    return {
        "message": "File uploaded successfully!",
        "filename": file.filename,
        **csv_info
    }
 

    
    
    
   