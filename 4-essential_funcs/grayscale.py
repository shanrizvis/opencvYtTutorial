import cv2 as cv

img = cv.imread("../resources/Photos/cat.jpg")

# convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Cat", gray)

capture = cv.VideoCapture(0)

while True:
    is_frame, frame = capture.read()

    cv.imshow("GreyMe", cv.cvtColor(frame, cv.COLOR_BGR2GRAY))
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
