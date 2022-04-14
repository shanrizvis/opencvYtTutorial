import cv2 as cv
import numpy as np

img = cv.imread("../resources/Photos/park.jpg")


# translation: shifting an image allong the x or y access
def translate(imgage, x_shift, y_shift):
    trans_matrix = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    dims = (imgage.shape[1], imgage.shape[0])
    return cv.warpAffine(imgage, trans_matrix, dims)


# note:
# -x => Left
# -y => up
# x => right
# y =>down


# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotmatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dims = (width, height)

    return cv.warpAffine(img, rotmatrix, dims)


# you can also dubbel rotate an image

# resize
resize = cv.resize(img, (5000, 5000), interpolation=cv.INTER_CUBIC)

# flip and mirror
flip = cv.flip(img, -1)

# cropping
cropped = img[200:400, 300:400]
cv.imshow("Crop", cropped)

cv.waitKey(0)
