# -*- coding: utf-8 -*-

import os
import cv2
import csv
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

PATH = 'img1-segment'

f = open('distance.csv', 'rb')
dist = []
for row in csv.reader(f):
    dist.append(int(row[2]))

f.close()

# Show Histogram

hist, bins = np.histogram(dist, bins=50)
width = 0.7 * (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
plt.bar(center, hist, align='center', width=width)
plt.show()
