import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import cv2

max_count = 0
max_x1 = 0
max_x2 = 0
for x1 in range(2, 15):
    for x2 in range(2, 15):
        count = 0
        for index in range(21000, 24499):
            img = cv2.imread('test/test/' + str(index) + '.jpg', 0)

            # Thresholding the image
            (thresh, img_bin) = cv2.threshold(img, 128, 255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
            # Invert the image
            if img_bin is None:
                continue
            img_bin = 255  - img_bin 
            #cv2.imwrite("Image_bin.jpg",img_bin)

            # %% [code]
            # Defining a kernel length
            kernel_length = np.array(img).shape[1] // 80

            # A verticle kernel of (1 X kernel_length), which will detect all the verticle lines from the image.
            verticle_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_length))
            # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
            hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 1))
            # A kernel of (3 X 3) ones.
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

            # %% [code]
            # Morphological operation to detect vertical lines from an image
            img_temp1 = cv2.erode(img_bin, verticle_kernel, iterations=x1)
            verticle_lines_img = cv2.dilate(img_temp1, verticle_kernel, iterations=x1)
            #cv2.imwrite("verticle_lines.jpg",verticle_lines_img)
            # Morphological operation to detect horizontal lines from an image
            img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=x2)
            horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=x2)
            #cv2.imwrite("horizontal_lines.jpg",horizontal_lines_img)

            # %% [code]
            # Weighting parameters, this will decide the quantity of an image to be added to make a new image.
            alpha = 0.5
            beta = 1.0 - alpha
            # This function helps to add two image with specific weight parameter to get a third image as summation of two image.
            img_final_bin = cv2.addWeighted(verticle_lines_img, alpha, horizontal_lines_img, beta, 0.0)
            img_final_bin = cv2.erode(~img_final_bin, kernel, iterations=2)
            (thresh, img_final_bin) = cv2.threshold(img_final_bin, 128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            #cv2.imwrite("img_final_bin.jpg",img_final_bin)

            # %% [code]
            # Find contours for image, which will detect all the boxes
            contours, hierarchy = cv2.findContours(img_final_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # Sort all the contours by top to bottom.
            #(contours, boundingBoxes) = sort_contours(contours, method="top-to-bottom")

            # %% [code]
            idx = 0
            # minx = float('inf')
            # maxx = 0
            # miny = float('inf')
            # maxy = 0
            closest = float("inf")
            coord = []
            ok = 0
            for c in contours:
                # Returns the location and width,height for every contour
                x, y, w, h = cv2.boundingRect(c)
                s = w * h
        #         print(s)
                if s > 2000 and s < 4500 :
                        count += 1
                if abs(s - 16000) < closest :
                    closest = abs(s - 16000)
                    coord = [x , y, w, h]
            x, y, h = coord[0], coord[1], coord[3]
            w = coord[2] // 4
        #     print(f"width = {w}")
        #     print(f"height {h}")
            fw = 5 * w // 100
            fh = 15 * h // 100
            for i in range(4):
                new_img = img[y + fh : y + h - fh, x + fw : x + w - fw]
                x = x + w
                #cv2.imwrite('bon' + str(i) + '.png', new_img)
        if count > max_count:
            max_count = count
            max_x1 = x1
            max_x2 = x2
print(f"max count = {max_count}")
print(f"max x1 = {max_x1}")
print(f"max x2 = {max_x2}")
