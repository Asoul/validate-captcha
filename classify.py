# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

PATH = 'classified'

def create_folder(path):
    if not os.path.isdir(path):
        os.mkdir(path)

def create_folders():
    create_folder(PATH)
    for n in range(0, 10):
        create_folder('{}/{}'.format(PATH, n))
    for ch in range(65, 91):
        create_folder('{}/{}'.format(PATH, chr(ch)))

create_folders()

def mse(img1, img2):
    return np.sum((img1 - img2) ** 2) / img1.size

# Load Sample Alphabets
targets = {}

for i in range(0, 10):
    targets[str(i)] = cv2.imread('sample-alphabet/{}.png'.format(i), 0)

for i in range(65, 91):
    targets[chr(i)] = cv2.imread('sample-alphabet/{}.png'.format(chr(i)), 0)

image_names = [name for name in os.listdir('img1-segment') if name[-4:] == '.png']

# Classify
for image_name in image_names:
    image = cv2.imread('img1-segment/{}'.format(image_name), 0)
    target_mse = [(ch, mse(image, targets[ch])) for ch in targets]
    result = min(target_mse, key=lambda x:x[1])[0]
    cv2.imwrite("{}/{}/{}.png".format(PATH, result, image_name), image)

