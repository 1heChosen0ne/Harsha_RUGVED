import cv2 as cv
img = cv.imread(r'C:\Users\vihas\PycharmProjects\PythonProject\task_3\photos\British_shorthair.png')
#cv.imshow('cat', img)
def rescaleFrame(frame, scale=2):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
cv.imshow('cat', rescaleFrame(img))
cv.waitKey(0)
#vid = cv.VideoCapture(r'C:\Users\vihas\PycharmProjects\PythonProject\task_3\Videos\5871756-hd_1080_1920_30fps.mp4')
#while True:
 #   isTrue, frame = vid.read()
 #   cv.imshow('Video', frame)
 #   if cv.waitKey(1) & 0xFF == ord('q'):
  #      break
#vid.release()
#cv.destroyAllWindows()





