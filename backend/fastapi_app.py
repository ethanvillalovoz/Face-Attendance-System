from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

# Import batch processing and database logic
from src.batch_attendance import process_image_folder
from backend.database.attendance_db import init_db, get_attendance_records

# Directory paths for storing images and attendance data
KNOWN_DIR = "data/known_faces"
BATCH_DIR = "data/batch_images"

# Ensure necessary directories exist
os.makedirs(KNOWN_DIR, exist_ok=True)
os.makedirs(BATCH_DIR, exist_ok=True)

# Initialize the database
init_db()

# Create FastAPI app instance
app = FastAPI(
    title="FaceTrack API",
    description="API for FaceTrack: Smart Face Recognition Attendance System",
    version="1.0.0"
)

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health"])
def read_root():
    """Health check endpoint."""
    return {"message": "FaceTrack FastAPI backend is running."}

@app.post("/upload/known/", tags=["Upload"])
async def upload_known_face(file: UploadFile = File(...)):
    """
    Upload a known face image.
    """
    file_location = os.path.join(KNOWN_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"Known face '{file.filename}' uploaded successfully."}

@app.post("/upload/batch/", tags=["Upload"])
async def upload_batch_image(file: UploadFile = File(...)):
    """
    Upload a batch image for attendance processing.
    """
    file_location = os.path.join(BATCH_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"Batch image '{file.filename}' uploaded successfully."}

@app.post("/process/", tags=["Processing"])
def process_batch():
    """
    Trigger batch face recognition and mark attendance.
    """
    process_image_folder(BATCH_DIR, KNOWN_DIR)
    return {"info": "Batch processing complete. Attendance marked."}

@app.get("/attendance/", tags=["Attendance"])
def get_attendance():
    """
    Retrieve all attendance records.
    """
    records = get_attendance_records()
    return {"attendance": [{"name": name, "timestamp": timestamp} for name, timestamp in records]}