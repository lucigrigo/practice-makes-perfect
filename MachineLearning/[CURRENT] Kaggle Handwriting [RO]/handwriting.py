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

# Hough transformation to detect lines
import cv2
import matplotlib.pyplot as plt
