"""
basics.py
Demonstrates basic face recognition: loading images, detecting faces, encoding, comparing, and visualizing results.
"""

import cv2
import numpy as np
import face_recognition

def load_and_prepare_image(image_path: str) -> np.ndarray:
    """
    Loads an image file and converts it from BGR to RGB.
    Args:
        image_path (str): Path to the image file.
    Returns:
        np.ndarray: The loaded and converted image.
    """
    img = face_recognition.load_image_file(image_path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def draw_face_rectangle(image: np.ndarray, face_location: tuple, color=(255, 0, 255), thickness=2) -> None:
    """
    Draws a rectangle around the detected face.
    Args:
        image (np.ndarray): The image to draw on.
        face_location (tuple): (top, right, bottom, left) coordinates.
        color (tuple): Rectangle color in BGR.
        thickness (int): Rectangle thickness.
    """
    top, right, bottom, left = face_location
    cv2.rectangle(image, (left, top), (right, bottom), color, thickness)

def main() -> None:
    """
    Loads two images, detects faces, compares them, and visualizes the result.
    """
    # Load and prepare images
    img_elon = load_and_prepare_image("data/image_basics_data/Elon_Musk.jpeg")
    img_elon_test = load_and_prepare_image("data/image_basics_data/Elon_Musk_Test.jpeg")

    # Detect face locations and encodings
    try:
        face_location = face_recognition.face_locations(img_elon)[0]
        face_encoding = face_recognition.face_encodings(img_elon)[0]
    except IndexError:
        print("No face found in Elon_Musk.jpeg")
        return

    try:
        face_location_test = face_recognition.face_locations(img_elon_test)[0]
        face_encoding_test = face_recognition.face_encodings(img_elon_test)[0]
    except IndexError:
        print("No face found in Elon_Musk_Test.jpeg")
        return

    # Draw rectangles around faces
    draw_face_rectangle(img_elon, face_location)
    draw_face_rectangle(img_elon_test, face_location_test)

    # Compare faces and calculate distance
    results = face_recognition.compare_faces([face_encoding], face_encoding_test)
    face_distance = face_recognition.face_distance([face_encoding], face_encoding_test)

    print("Face distance:", face_distance)
    print("Is the test image a match?", results[0])

    # Annotate test image with results
    cv2.putText(
        img_elon_test,
        f"Match: {results[0]} - Distance: {face_distance[0]:.2f}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Display images
    cv2.imshow("Elon Musk", img_elon)
    cv2.imshow("Elon Musk Test", img_elon_test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()