import cv2 as cv

# ouvri kamera // open camera
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    isTrue, frame = cap.read()
    cv.imshow("Roadster", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
