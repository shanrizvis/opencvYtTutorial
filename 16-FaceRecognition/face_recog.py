import os
import cv2 as cv
import numpy as np

PEEPS = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

PATH = r"data/train"

features = []
labels = []

haar_cascade = cv.CascadeClassifier("haar_face.xml")


def fill_train():
    for peep in PEEPS:
        person_path = os.path.join(PATH, peep)
        label = PEEPS.index(peep)

        for img in os.listdir(person_path):
            img_path = os.path.join(person_path, img)
            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)
            face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in face_rect:
                region = gray[y:y + h, x:x + w]
                features.append(region)
                labels.append(label)


fill_train()

features = np.array(features)
labels = np.array(labels)

recog = cv.face.LBPHFaceRecognizer_create()
recog.train(features, labels)
