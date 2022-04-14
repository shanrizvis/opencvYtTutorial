import cv2 as cv
import numpy as np

# bluring is done using convolution
# we use a matrix to change the image
# we have different methods to achieve this
img = cv.imread("../resources/Photos/cats 2.jpg")

# average blur
blur = cv.blur(img, (3, 3))

# gaussian blur
# this is usually less blurred
blur = cv.GaussianBlur(img, (3, 3), 0)

# median blur
# will blur a bit more
blur = cv.medianBlur(img, 3)

# bilateral
# you keep the edges
blur = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Blurred", blur)

cv.waitKey(0)
