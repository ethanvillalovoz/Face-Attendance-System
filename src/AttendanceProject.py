import cv2
import numpy as np
import face_recognition
import os

path = "data/image_attendance_data"
images = []
classNames = []
my_list = os.listdir(path)
print(my_list)
for cl in my_list:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)