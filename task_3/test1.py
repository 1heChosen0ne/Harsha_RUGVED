import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\vihas\PycharmProjects\PythonProject\task_3\photos\British_shorthair.png')
canny = cv.Canny(img,125, 175)
cv.imshow('Canny  Edges',canny)
cv.waitKey(0)