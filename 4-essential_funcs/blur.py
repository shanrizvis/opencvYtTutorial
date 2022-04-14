import cv2 as cv

img = cv.imread("../resources/Photos/cat.jpg")

# convert image to grayscale
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

cv.imshow("Blurry", blur)

cv.waitKey(0)
