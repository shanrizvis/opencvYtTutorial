import cv2 as cv


img = cv.imread('../resources/Photos/cat.jpg')
cv.imshow("Cat", img)

# wait inf time for key to be pressed
cv.waitKey(0)