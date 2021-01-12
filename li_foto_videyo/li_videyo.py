import cv2 as cv

# li videyo // read videos
cap = cv.VideoCapture('resous/videyo/Roadster.mp4')

while True:
    isTrue, frame = cap.read()
    cv.imshow("Roadster", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
