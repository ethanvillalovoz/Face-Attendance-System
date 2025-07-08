# FaceTrack: Smart Face Recognition Attendance System

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![React](https://img.shields.io/badge/frontend-React-blue)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-green)

---

## 🚀 Introduction

**FaceTrack** is a modern, full-stack face recognition attendance system. It enables organizations to automate attendance logging using face recognition, providing a seamless and contactless experience.

---

## 📖 Description

FaceTrack allows users to:
- Upload known face images (for registration)
- Upload batch images (for attendance sessions)
- Process batches to recognize faces and mark attendance
- View and download attendance records

The system uses a React frontend, FastAPI backend, and a SQLite database for robust, real-time attendance management.

---

## 🖼️ Visuals

![FaceTrack UI Screenshot](docs/screenshots/home_page.png)
*Main dashboard: Upload, process, and view attendance records.*

---

## 🛠️ Prerequisites / Requirements

- **Python 3.8+** (for backend)
- **Node.js 16+ & npm** (for frontend)
- **conda** (optional, for environment management)
- **OpenCV, face_recognition, FastAPI, Uvicorn** (see requirements.txt)
- **LFW dataset** (optional, for demo/testing)

---

## ⚙️ Technologies Used

- **Frontend:** React, CSS
- **Backend:** FastAPI, Uvicorn
- **Face Recognition:** face_recognition, OpenCV
- **Database:** SQLite
- **Other:** Python standard libraries

---

## ⚡ QuickStart Guide

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/face-attendance-system.git
cd face-attendance-system
```

### 2. Set up the backend

```bash
pip install -r requirements.txt
uvicorn backend.fastapi_app:app --reload
```

### 3. Set up the frontend

```bash
cd frontend
npm install
npm start
```

### 4. Access the application

- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`

---

## 📂 Folder Structure & Purpose

```
face-attendance-system/
│
├── backend/               # Backend application (FastAPI)
│   ├── database/          # Database logic and SQLite integration
│   └── fastapi_app.py     # FastAPI entry point and API endpoints
│
├── frontend/              # Frontend application (React)
│   ├── public/            # Static assets for React
│   ├── src/               # React source code (components, styles)
│   └── package.json       # npm configuration and dependencies
│
├── src/                   # Core Python scripts for face recognition
│   ├── AttendanceProject.py   # Webcam-based attendance logic
│   ├── batch_attendance.py   # Batch image attendance processing
│   ├── basics.py             # Basic face recognition demo
│   └── sample_lfw_images.py  # Utility for sampling LFW images
│
├── data/                  # Data storage for images and attendance
│   ├── known_faces/           # Uploaded known face images
│   ├── batch_images/          # Uploaded batch images for attendance
│   ├── Attendance.csv         # (Legacy) CSV attendance log
│   ├── image_attendance_data/ # Images for webcam attendance demo
│   ├── image_basics_data/     # Images for basics.py demo
│   └── lfw/                   # LFW dataset for testing/demo
│
├── docs/                  # Documentation and screenshots
│   ├── screenshots/           # UI screenshots for README/docs
│   └── ...                    # Other documentation files
│
├── .gitignore             # Git ignore file
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

### **Folder Purpose Summary**

- **backend/**: All backend logic, API, and database code.
- **frontend/**: All frontend React code and static assets.
- **src/**: Python scripts for face recognition, attendance, and utilities.
- **data/**: Stores all images, attendance logs, and datasets used by the system.
- **docs/**: Documentation and visuals for the project.
- **.gitignore, README.md, requirements.txt**: Standard project files for setup and documentation.

---

## 🔌 API Endpoints Overview

| Endpoint                | Method | Purpose                                              |
|-------------------------|--------|------------------------------------------------------|
| `/upload/known/`        | POST   | Upload a known face image for registration           |
| `/upload/batch/`        | POST   | Upload a batch image for attendance processing       |
| `/process/`             | POST   | Trigger batch face recognition and mark attendance   |
| `/attendance/`          | GET    | Retrieve all attendance records                      |
| `/`                     | GET    | Health check for backend                             |

All endpoints are available at `http://localhost:8000` by default.

---

## ❓ Troubleshooting / FAQ

**Q: The frontend can't connect to the backend.**  
A: Ensure the backend is running (`uvicorn backend.fastapi_app:app --reload`) and CORS is enabled. The default CORS settings allow all origins.

**Q: No faces are recognized in uploaded images.**  
A: Make sure you have uploaded clear, front-facing images for both known and batch sets. Check that the image files are not corrupted.

**Q: I get a "ModuleNotFoundError" or missing dependency error.**  
A: Double-check that you've installed all Python and Node.js dependencies using `pip install -r requirements.txt` and `npm install`.

**Q: How do I get the LFW dataset for testing?**  
A: Download the LFW dataset from [https://www.kaggle.com/datasets/jessicali9530/lfw-dataset](https://www.kaggle.com/datasets/jessicali9530/lfw-dataset?resource=download) and extract it to `data/lfw/`.

**Q: CORS or network errors in the browser console.**  
A: Make sure both frontend (`npm start`) and backend (`uvicorn ...`) are running, and that you are accessing the correct ports.

---

## 📫 Contact / Support

- For issues, feature requests, or questions, please [open an issue](https://github.com/ethanvillalovoz/Face-Attendance-System/tree/main/.github/ISSUE_TEMPLATE) on GitHub.

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
