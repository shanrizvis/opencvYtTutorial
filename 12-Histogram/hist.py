import cv2 as cv
import matplotlib.pyplot as plt

# we can create a histogram to see the
# distribution of pixels in an image


img = cv.imread("../resources/Photos/cats.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale")
plt.xlabel("Intensity")
plt.ylabel("# of labels")
plt.plot(gray_hist)

cv.waitKey(0)
