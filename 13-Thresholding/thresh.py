import cv2 as cv

# we binary an image
# we set a treshold and look
# if its above or below

img = cv.imread("../resources/Photos/cats.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# simple thresholding
treshold, tresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)


# using this we can create an inverse threshold
treshold, tresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)

# adaptive
# we need to set a tresh ourselfs
# we can use this to let the computer set a tresh valUe
adaptive = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 5,3)

cv.imshow("treshholded", adaptive)
cv.waitKey(0)
