import cv2 as cv

# to detect a face we use a haarcascade
# this works by detecting edges and classifying it

img = cv.imread("../resources/Photos/group 1.jpg")

# because color is not needed we transform it into a gray image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# the classifier
haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rects = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

# cv.imshow("lady", gray)
print(f"Number of faces = {len(faces_rects)}")

# this is actualle the rectangular coordinates of a face so we
# can loop and draw a rectangle

for (x, y, w, h) in faces_rects:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Face", img)
cv.waitKey(0)
