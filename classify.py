# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def mse(img1, img2):
    return np.sum((img1 - img2) ** 2) / img1.size

# Load Sample Alphabets
targets = {}

for i in range(0, 10):
    image = cv2.imread('sample-alphabet/{}.png'.format(i))
    targets[str(i)] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for i in range(65, 91):
    image = cv2.imread('sample-alphabet/{}.png'.format(chr(i)))
    targets[chr(i)] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Classify
for img_index in range(0, 1):
    img_index = str(img_index).zfill(4)

    image = cv2.imread('collect-recaptcha/img/{}.jpg'.format(img_index))

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

    # Find bounding rect
    bounding_rects = [cv2.boundingRect(c) for c in contours]
    choosed_rects = [c for c in bounding_rects if c[2] > 15 and c[3] > 15]
    choosed_rects.sort(key=lambda x: x[0])

    # Save segmented image
    for char_index, (x, y, w, h) in enumerate(choosed_rects):
        resized = cv2.resize(dilation[y : y + h, x : x + w], (50, 50))
        likelihoods = [(ch, mse(resized, targets[ch])) for ch in targets]
        print likelihoods
        result = max(likelihoods, key=lambda x:x[1])[0]
        # cv2.imwrite("classified/{}/{}-{}.png".format(result, img_index, char_index), resized)

