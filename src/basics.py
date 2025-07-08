import cv2
import numpy as np
import face_recognition

img_Elon_Musk = face_recognition.load_image_file("image_basics_data/Elon_Musk.jpeg")
img_Elon_Musk = cv2.cvtColor(img_Elon_Musk, cv2.COLOR_BGR2RGB)

img_Elon_Musk_test = face_recognition.load_image_file("image_basics_data/Elon_Musk_Test.jpeg")
img_Elon_Musk_test = cv2.cvtColor(img_Elon_Musk_test, cv2.COLOR_BGR2RGB)

cv2.imshow("Elon Musk", img_Elon_Musk)
cv2.imshow("Elon Musk Test", img_Elon_Musk_test)
cv2.waitKey(0)