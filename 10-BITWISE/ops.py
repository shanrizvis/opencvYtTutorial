import cv2 as cv

# a pixel is turned off if it is 0
# a pixel is turned on if it is 1
# this is binary meaning we can use the
# bitwise operators
import numpy as np

img = cv.imread("../resources/Photos/cat.jpg")
blank = np.zeros((400, 400), dtype="uint8")

rect = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255,-1)


# bitwise and
b_and = cv.bitwise_and(rect, circle)

# bitwise or
b_or = cv.bitwise_or(rect, circle)

# bitwise xor
b_xor = cv.bitwise_xor(rect, circle)

# bitwise not
# this will invert everything
b_not = cv.bitwise_not(rect)
cv.imshow("bit", b_not)

cv.waitKey(0)
