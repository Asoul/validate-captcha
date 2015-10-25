# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = 'img1-segment'

if not os.path.isdir(PATH):
    os.mkdir(PATH)

for img_index in range(0, 10000):

    image = cv2.imread('collect-recaptcha/img/{}.jpg'.format(str(img_index).zfill(4)))

    # Erode noise
    kernel = np.ones((4, 4), np.uint8)
    erosion = cv2.erode(image, kernel, iterations = 1)

    # Blur border
    blurred = cv2.GaussianBlur(erosion, (5, 5), 0)

    # Find edge
    edged = cv2.Canny(blurred, 30, 150)

    # Dilate content
    dilation = cv2.dilate(edged, kernel, iterations = 1)

    # Find contours
    contours = cv2.findContours(dilation.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]

    # Find bounding rect, only choose larger than 15 x 15
    bounding_rects = [cv2.boundingRect(c) for c in contours]
    choosed_rects = [c for c in bounding_rects if c[2] > 15 and c[3] > 15]
    choosed_rects.sort(key=lambda x: x[0])

    # Save segmented image
    for char_index, (x, y, w, h) in enumerate(choosed_rects):
        # Skip contain more than 1 alphabet
        if w > 50:
            continue
        # Skip contour inside contour
        if char_index > 1:
            last_x, last_y, last_w, last_h = choosed_rects[char_index - 1]
            if last_x <= x <= x + h <= last_x + last_h:
                continue

        resized = cv2.resize(dilation[y : y + h, x : x + w], (50, 50))
        cv2.imwrite("{}/{}-{}.png".format(PATH, str(img_index).zfill(4) , char_index), resized)

