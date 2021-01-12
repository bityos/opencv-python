import cv2 as cv

# li imaj // read images
foto = cv.imread('resous/foto/posh.jpg')

cv.imshow('posh', foto)
cv. waitKey(0)
