import cv2 as cv

img = cv.imread("../resources/Photos/cat.jpg")

# convert image to grayscale
canny = cv.Canny(img, 125, 175)
dilate = cv.dilate(canny, (3, 3), iterations=3)
cv.imshow("Dilate", dilate)

cv.waitKey(0)
