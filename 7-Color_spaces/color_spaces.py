import cv2 as cv
import numpy as np

# there are many colorspaces like rbg brg..
# these can be converted from or to


img = cv.imread("../resources/Photos/group 1.jpg")

# bgr to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# bgr to hsv
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# bgr to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# bgr to rgb
# has to be done for some images because the colors will be inverted
# in other programs like matplotlib
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# all inverse are possible
# but sometimes you have to go to bgr to go to another
# eg gray to hsv is not possible => first go to bgr then hsv

cv.imshow("color space", rgb)

cv.waitKey(0)
