from app.services.cleaner import clean_csv
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path
import shutil

from app.core.settings import settings


router = APIRouter()
router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "CSV Cleaner API is running."
    }


@router.post("/upload")
def upload_csv(file: UploadFile = File(...)):
    upload_dir = Path(settings.UPLOAD_DIR)
    upload_dir.mkdir(exist_ok=True)

    file_path = upload_dir / file.filename

    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    cleaning_report = clean_csv(file_path)
    cleaned_file = cleaning_report.pop("output_path")

    return {
        "message": "CSV cleaned successfully!",
        "filename": file.filename,
        **cleaning_report,
        "download_url": f"/download/{Path(cleaned_file).name}"
    }


@router.get("/download/{filename}")
def download_file(filename: str):
    file_path = Path("app/data/cleaned") / filename

    if not file_path.exists():
        return {"error": "File not found"}

    return FileResponse(
        path=file_path,
        media_type="text/csv",
        filename=filename
    )
