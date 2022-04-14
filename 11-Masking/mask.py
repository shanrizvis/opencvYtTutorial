import cv2 as cv

# using bitwise operators we can do masking
# this can be done to remove or only focus on special places

import numpy as np

img = cv.imread("../resources/Photos/cats.jpg")
blank = np.zeros(img.shape[:2], dtype="uint8")  # has to be same size!

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

mask_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked", mask_image)

cv.waitKey(0)
