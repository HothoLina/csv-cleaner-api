from app.services.cleaner import clean_csv
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
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
        cleaning_report = clean_csv(file_path)
    except Exception as e:
        return {"message": "File uploaded but failed to read CSV", "error": str(e)}

    cleaned_file = cleaning_report.pop("output_path")

    return {
        "message": "CSV cleaned successfully!",
        "filename": file.filename,
        **cleaning_report,
        "download_url": f"/download/{Path(cleaned_file).name}"
    }


@router.get("/download/{filename}")
def download_file(filename: str):
    file_path = Path("cleaned") / filename

    if not file_path.exists():
        return {"error": "File not found"}

    return FileResponse(
        path=file_path,
        media_type="text/csv",
        filename=filename
    )