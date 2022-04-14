import cv2 as cv

# you can give a path or an integer
# integer will use the webcam
# a path will show the video

capture = cv.VideoCapture('../resources/Videos/dog.mp4')
# capture = cv.VideoCapture(0)

while True:
    # we grab the video frame and see if this capture is successful
    is_true, frame = capture.read()

    # if this is successful then we will display the grabbed frame
    cv.imshow('Video', frame)

    # we break when when the letter d is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    # if we give the wrong path or the video ends then we get an error
    # and the program will end

capture.release()
cv.destroyAllWindows()
