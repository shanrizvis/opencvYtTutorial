import cv2 as cv
import numpy as np

# how to find edges


capture = cv.VideoCapture(0)

while True:
    is_true, frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # laplacian
    lap = cv.Laplacian(gray, cv.CV_64F)
    lap = np.uint8(np.absolute(lap))

    # sobel
    sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
    sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
    sobel = cv.bitwise_or(sobely, sobelx)
    cv.imshow('Video', sobel)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
