import cv2 as cv
import numpy as np

# we can draw in 2 ways
# 1.We draw directly on the image
# 2.We create a blank image and draw on that

# blank image
# we create a blank image with a certain size
# the datatype must be unint8
blank = np.zeros((500, 500, 3), dtype="uint8")

# we can set its color
# blank[:] = (0, 0, 255)

# we can color a certain range of pixels
# blank[200:300, 300:400] = (0, 0, 255)

# this will draw a green rectangle
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)

# we can also draw a circle
cv.circle(blank, (250, 250), 50, (0, 0, 255), thickness=3)

# or a line
cv.line(blank, (0, 0), (250, 250), (255, 0, 0), thickness=4)

# and of course text
cv.putText(blank, "Hello world!", (300, 300), cv.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), 2)
cv.imshow("Green", blank)

cv.waitKey(0)
