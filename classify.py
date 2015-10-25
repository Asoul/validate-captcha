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

def loadImage(path):
    image = cv2.imread(path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(gray_image, 127, 255, 0)[1]

# Load Sample Alphabets
targets = {}

for i in range(0, 10):
    targets[str(i)] = loadImage('sample-alphabet/{}.png'.format(i))

for i in range(65, 91):
    targets[chr(i)] = loadImage('sample-alphabet/{}.png'.format(chr(i)))

image_names = [name for name in os.listdir('img1-segment') if name[-4:] == '.png']

# Classify
for image_name in image_names:
    image = loadImage('img1-segment/{}'.format(image_name))
    target_mse = [(ch, mse(image, targets[ch])) for ch in targets]
    result = min(target_mse, key=lambda x:x[1])[0]
    cv2.imwrite("{}/{}/{}.png".format(PATH, result, image_name), image)

