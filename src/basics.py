import cv2
import numpy as np
import face_recognition

img_Elon_Musk = face_recognition.load_image_file("image_basics_data/Elon_Musk.jpeg")
img_Elon_Musk = cv2.cvtColor(img_Elon_Musk, cv2.COLOR_BGR2RGB)

img_Elon_Musk_test = face_recognition.load_image_file("image_basics_data/Elon_Musk_Test.jpeg")
img_Elon_Musk_test = cv2.cvtColor(img_Elon_Musk_test, cv2.COLOR_BGR2RGB)

face_locations = face_recognition.face_locations(img_Elon_Musk)[0]
face_encodings = face_recognition.face_encodings(img_Elon_Musk)[0]
cv2.rectangle(img_Elon_Musk, 
              (face_locations[3], face_locations[0]), 
              (face_locations[1], face_locations[2]), 
              (255, 0, 255), 
              2)

face_locations_test = face_recognition.face_locations(img_Elon_Musk_test)[0]
face_encodings_test = face_recognition.face_encodings(img_Elon_Musk_test)[0]
cv2.rectangle(img_Elon_Musk_test, 
              (face_locations_test[3], face_locations_test[0]), 
              (face_locations_test[1], face_locations_test[2]), 
              (255, 0, 255), 
              2)

results = face_recognition.compare_faces([face_encodings], face_encodings_test)
face_distance = face_recognition.face_distance([face_encodings], face_encodings_test)
print("Face distance: ", face_distance)
print("Is the test image a match? ", results[0])

cv2.putText(img_Elon_Musk_test, 
            f"Match: {results[0]} - Distance: {face_distance[0]:.2f}", 
            (50, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1, 
            (0, 0, 255), 
            2)
cv2.imshow("Elon Musk", img_Elon_Musk)
cv2.imshow("Elon Musk Test", img_Elon_Musk_test)
cv2.waitKey(0)