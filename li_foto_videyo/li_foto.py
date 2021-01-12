import cv2 as cv

# li imaj // read images
img = cv.imread('resous/foto/posh.jpg')

cv.imshow('posh', img)
cv. waitKey(0)
