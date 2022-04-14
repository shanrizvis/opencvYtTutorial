import cv2 as cv

img = cv.imread("../resources/Photos/cat.jpg")

# convert image to grayscale
canny = cv.Canny(img, 125,175)

# cv.imshow("Blurry", canny)

capture = cv.VideoCapture(0)
while True:
    is_true, frame = capture.read()
    cv.imshow('Video', cv.Canny(frame, 125,175))

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    # if we give the wrong path or the video ends then we get an error
    # and the program will end

capture.release()
cv.destroyAllWindows()