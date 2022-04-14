import cv2 as cv


# we calculate new dimensions and resize the image
# this also works for video frames
def rescale(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dims = (width, height)
    return cv.resize(frame, dims, interpolation=cv.INTER_AREA)


img = cv.imread('../resources/Photos/cat_large.jpg')
cv.imshow('Cat', rescale(img, 0.25))

cv.waitKey(0)

capture = cv.VideoCapture('../resources/Videos/dog.mp4')

while True:
    is_true, frame = capture.read()
    cv.imshow('Video', rescale(frame, 0.50))

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


# for videos you can also use set
# this only works for live video!
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)


capture.release()
cv.destroyAllWindows()
