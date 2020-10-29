# RECUNOASTEREA SCRISULUI DE MANA

# importing libraries
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from copy import copy
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

def apply_filter(img):
    result = copy(img)
    for i in range(1, len(img) - 2):
        for j in range(1, len(img[0]) - 2):
            s = 0
            s = int(img[i][j - 1]) + int(img[i - 1][j]) + int(img[i][j + 1]) + int(img[i + 1][j])
            if img[i][j] == 255 and s <= 765:
                result[i][j] = 0
    return result


# importing train and test set csv files
train_set_csv = pd.read_csv('train.csv')
test_set_csv = pd.read_csv('sampleSubmission.csv')

# importing train set images
train_set = dict()
for index in range(20000, 22000):
    filename = str(index) + '.jpg'
    img = cv2.imread('train/train/' + filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    img_bin = apply_filter(img_bin)
    img_bin = 255  - img_bin 
    
    # Defining a kernel length
    kernel_length = np.array(img).shape[1] // 80
    
    # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Morphological operation to detect vertical lines from an image
    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=7)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=7)
    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=7)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=7)
    
    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.5
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (_, img_final_bin) = cv2.threshold(img_final_bin, 150,255, cv2.THRESH_BINARY)
    cv2.imwrite("img_final_bin.jpg",img_final_bin)
    
    # Find contours for image, which will detect all the boxes
    contours, _ = cv2.findContours(img_final_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    cur_imgs = []
    closest = float("inf")
    coord = None
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        s = w * h
        if abs(s - 18500) < closest :
            closest = abs(s - 18500)
            coord = [x , y, w, h]
    
    s = coord[2] * coord[3]
    if s > 21000 or s < 11000:
        count_sq = 0
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            s = w * h
            if s > 2000 and s < 4500:
                count_sq += 1
                new_img = img[y : y + h, x : x + w]
                cur_imgs.append(new_img)
        if count_sq != 4:
            cur_imgs = None
    else:
        x, y, h = coord[0], coord[1], coord[3]
        w = coord[2] // 4
        fw = 5 * w // 100
        fh = 15 * h // 100
        for i in range(4):
            new_img = img[y + fh : y + h - fh, x + fw : x + w - fw]
            cur_imgs.append(new_img)
            x = x + w
    
    train_set[filename] = cur_imgs

# importing test set images
test_set = dict()
for index in range(22000, 24499):
    filename = str(index) + '.jpg'
    img = cv2.imread('test/test/' + filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img_bin = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    img_bin = apply_filter(img_bin)
    img_bin = 255  - img_bin 
    
    # Defining a kernel length
    kernel_length = np.array(img).shape[1] // 80
    
    # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
    verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Morphological operation to detect vertical lines from an image
    img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=7)
    verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=7)
    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=7)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=7)
    
    # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
    alpha = 0.5
    beta = 1.0 - alpha
    # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
    img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
    img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
    (_, img_final_bin) = cv2.threshold(img_final_bin, 150,255, cv2.THRESH_BINARY)
    cv2.imwrite("img_final_bin.jpg",img_final_bin)
    
    # Find contours for image, which will detect all the boxes
    contours, _ = cv2.findContours(img_final_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    cur_imgs = []
    closest = float("inf")
    coord = None
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        s = w * h
        if abs(s - 18500) < closest :
            closest = abs(s - 18500)
            coord = [x , y, w, h]
    
    s = coord[2] * coord[3]
    if s > 21000 or s < 11000:
        count_sq = 0
        for c in contours:
            x, y, w, h = cv2.boundingRect(c)
            s = w * h
            if s > 2000 and s < 4500:
                count_sq += 1
                new_img = img[y : y + h, x : x + w]
                cur_imgs.append(new_img)
        if count_sq != 4:
            cur_imgs = None
    else:
        x, y, h = coord[0], coord[1], coord[3]
        w = coord[2] // 4
        fw = 5 * w // 100
        fh = 15 * h // 100
        for i in range(4):
            new_img = img[y + fh : y + h - fh, x + fw : x + w - fw]
            cur_imgs.append(new_img)
            x = x + w
    
    test_set[filename] = cur_imgs

# eliminating None type entries
k_elim = []
for k, v in train_set.items():
    if v == None:
        k_elim.append(k)
        train_set_csv = train_set_csv[train_set_csv['Id'] != k]
for k in k_elim:
    train_set.pop(k)

k_elim = []
for k, v in test_set.items():
    if v == None:
        k_elim.append(k)
        test_set_csv = test_set_csv[test_set_csv['Id'] != k]
for k in k_elim:
    test_set.pop(k)
    
# building the CNN
# Initialising the CNN
classifier = Sequential()

classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Additional layer added
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Aditional layer added
classifier.add(Convolution2D(32, 3, 3, activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full connection
classifier.add(Dense(128, activation = 'relu'))
classifier.add(Dense(1, activation = 'sigmoid'))

# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

        
        
        
        
        
        
        
        
        