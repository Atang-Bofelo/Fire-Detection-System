import cv2
from cv2 import VideoCapture
from cv2 import waitKey
print(cv2.__version__)

video = cv2.videoCapture("video.mov")
while True:
    ret, frame = video.read()
    frame = cv2.resize(frame, (1000, 600))

    if ret == False:
        break

    cv2.imshow("Output", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
video.release()

