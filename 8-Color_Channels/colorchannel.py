import cv2 as cv
import numpy as np

# there are color channels
# we can split these parts of the image
# and only show those colors
# these are displayed as grayscale image
# with white meaning more of that color and black less of that

img = cv.imread("../resources/Photos/group 1.jpg")

b, g, r = cv.split(img)

# cv.imshow("Red color", r)
# cv.imshow("green color", g)
# cv.imshow("Blue color", b)

# we can merge these channels again to form the original
merged = cv.merge([b, g, r])

# to see the non grayscale version we have to do an extra step
# using a blank image
# the more of the color the more of it was there

blank = np.zeros(img.shape[:2], dtype="uint8")
blue_image = cv.merge([b, blank, blank])
green_image = cv.merge([blank, g, blank])
red_image = cv.merge([blank, blank, r])

cv.imshow("Red color", blue_image)
cv.imshow("green color", green_image)
cv.imshow("Blue color", red_image)

cv.waitKey(0)
