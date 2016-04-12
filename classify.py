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

def distance(img1, img2):
    return np.sum(abs(img1.astype('int') - img2.astype('int'))/255)


def load_sample_alphabets(folder="sample-alphabet"):
    '''Load Sample Alphabets from /sample-alphabet'''
    targets = {}

    for i in range(0, 10):
        targets[str(i)] = cv2.imread('{}/{}.png'.format(folder, i), 0)

    for i in range(65, 91):
        targets[chr(i)] = cv2.imread('{}/{}.png'.format(folder, chr(i)), 0)

    return targets


def main():
    create_folders()
    image_names = [name for name in os.listdir('img1-segment')
                   if name.endswith('.png')]

    # Classify
    for image_name in image_names:
        image = cv2.imread('img1-segment/{}'.format(image_name), 0)
        target_distances = [(ch, distance(image, targets[ch])) for ch in targets]
        outcome_char = min(target_distances, key=lambda x: x[1])[0]
        cv2.imwrite("{}/{}/{}".format(PATH, outcome_char, image_name), image)

if __name__ == '__main__':
    main()