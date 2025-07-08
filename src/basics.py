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

cv2.imshow("Elon Musk", img_Elon_Musk)
cv2.imshow("Elon Musk Test", img_Elon_Musk_test)
cv2.waitKey(0)