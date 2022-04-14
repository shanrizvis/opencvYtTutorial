import cv2 as cv
import numpy as np

img = cv.imread("../resources/Photos/cat.jpg")

# contours are the boundaries of objects
# these are the lines/curves that join the points
# these are not the same as edges!

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(blur, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape[:2], dtype="uint8")

cv.drawContours(blank, contours, -1, (255, 255, 255), 2)
cv.imshow("Contours", blank)
cv.waitKey(0)
