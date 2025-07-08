import os
import cv2
import numpy as np
import face_recognition
from datetime import datetime

from src.AttendanceProject import load_images_from_folder, find_encodings
from backend.database.attendance_db import mark_attendance_db

def process_image_folder(input_folder, known_images_folder):
    """
    Processes all images in the input_folder, detects and recognizes faces,
    and marks attendance for recognized individuals.
    """
    # Load known images and encodings
    known_images, class_names = load_images_from_folder(known_images_folder)
    known_encodings = find_encodings(known_images)
    print("Loaded known faces.")

    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Could not read {filename}, skipping.")
            continue
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(img_rgb)
        face_encodings = face_recognition.face_encodings(img_rgb, face_locations)
        for encode_face, face_loc in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, encode_face)
            face_dis = face_recognition.face_distance(known_encodings, encode_face)
            match_index = np.argmin(face_dis) if face_dis.size > 0 else None
            if match_index is not None and matches[match_index]:
                name = class_names[match_index]
                print(f"Recognized {name} in {filename}")
                mark_attendance_db(name)  # <-- Use DB function here
            else:
                print(f"Unknown face detected in {filename}")

if __name__ == "__main__":
    # Example usage:
    input_folder = "data/batch_images"  # Folder with images to process
    known_images_folder = "data/known_faces"  # Folder with known faces
    process_image_folder(input_folder, known_images_folder)
    print("Batch processing complete.")
