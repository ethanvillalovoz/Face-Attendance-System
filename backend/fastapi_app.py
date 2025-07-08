from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

# Import your batch processing logic
from src.batch_attendance import process_image_folder
from backend.database.attendance_db import init_db, get_attendance_records

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

KNOWN_DIR = "data/known_faces"
BATCH_DIR = "data/batch_images"
ATTENDANCE_FILE = "data/Attendance.csv"

os.makedirs(KNOWN_DIR, exist_ok=True)
os.makedirs(BATCH_DIR, exist_ok=True)

init_db()

@app.get("/")
def read_root():
    return {"message": "Face Attendance FastAPI is running."}

@app.post("/upload/known/")
async def upload_known_face(file: UploadFile = File(...)):
    file_location = os.path.join(KNOWN_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"Known face '{file.filename}' uploaded successfully."}

@app.post("/upload/batch/")
async def upload_batch_image(file: UploadFile = File(...)):
    file_location = os.path.join(BATCH_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"info": f"Batch image '{file.filename}' uploaded successfully."}

@app.post("/process/")
def process_batch():
    process_image_folder(BATCH_DIR, KNOWN_DIR)
    return {"info": "Batch processing complete. Attendance marked."}

@app.get("/attendance/")
def get_attendance():
    records = get_attendance_records()
    return {"attendance": [{"name": name, "timestamp": timestamp} for name, timestamp in records]}