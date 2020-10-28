# RECUNOASTEREA SCRISULUI DE MANA

# importing libraries
import numpy as np
import pandas as pd

# importing train and test set images
from PIL import Image
import glob
train_set = []
for filename in glob.glob('train/train/*.jpg'):
    img = Image.open(filename)
    train_set.append(img)
test_set = []
for filename in glob.glob('test/test/*.jpg'):
    img = Image.open(filename)
    test_set.append(img)

# importing train and test set csv files
train_set_csv = pd.read_csv('train.csv')
test_set_csv = pd.read_csv('sampleSubmission.csv')

# hough transformation to detect lines
import cv2 as cv
import math

src = cv.imread('train/train/20000.jpg')

dst = cv.Canny(src, 50, 200, None, 3)

cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)

lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
        
cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)