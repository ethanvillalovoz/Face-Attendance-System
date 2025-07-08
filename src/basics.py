import cv2
import numpy as np
import face_recognition

def load_and_prepare_image(image_path):
    """
    Loads an image file and converts it from BGR to RGB.
    """
    img = face_recognition.load_image_file(image_path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def draw_face_rectangle(image, face_location, color=(255, 0, 255), thickness=2):
    """
    Draws a rectangle around the detected face.
    """
    top, right, bottom, left = face_location
    cv2.rectangle(image, (left, top), (right, bottom), color, thickness)

def main():
    # Load and prepare images
    img_Elon_Musk = load_and_prepare_image("data/image_basics_data/Elon_Musk.jpeg")
    img_Elon_Musk_test = load_and_prepare_image("data/image_basics_data/Elon_Musk_Test.jpeg")

    # Detect face locations and encodings
    face_location = face_recognition.face_locations(img_Elon_Musk)[0]
    face_encoding = face_recognition.face_encodings(img_Elon_Musk)[0]

    face_location_test = face_recognition.face_locations(img_Elon_Musk_test)[0]
    face_encoding_test = face_recognition.face_encodings(img_Elon_Musk_test)[0]

    # Draw rectangles around faces
    draw_face_rectangle(img_Elon_Musk, face_location)
    draw_face_rectangle(img_Elon_Musk_test, face_location_test)

    # Compare faces and calculate distance
    results = face_recognition.compare_faces([face_encoding], face_encoding_test)
    face_distance = face_recognition.face_distance([face_encoding], face_encoding_test)

    print("Face distance:", face_distance)
    print("Is the test image a match?", results[0])

    # Annotate test image with results
    cv2.putText(
        img_Elon_Musk_test,
        f"Match: {results[0]} - Distance: {face_distance[0]:.2f}",
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    # Display images
    cv2.imshow("Elon Musk", img_Elon_Musk)
    cv2.imshow("Elon Musk Test", img_Elon_Musk_test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()