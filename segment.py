# -*- coding: utf-8 -*-

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

IMG_PATH = 'collect-captcha/img'
SAVE_PATH = 'img1-segment'

def main():
    if not os.path.isdir(SAVE_PATH):
        os.mkdir(SAVE_PATH)

    for img_index in range(0, 10000):

        image = cv2.imread('{}/{}.jpg'.format(IMG_PATH, str(img_index).zfill(4)))

        # Erode noise
        kernel = np.ones((4, 4), np.uint8)
        erosion = cv2.erode(image, kernel, iterations=1)

        # Blur border
        blurred = cv2.GaussianBlur(erosion, (5, 5), 0)

        # Find edge
        edged = cv2.Canny(blurred, 30, 150)

        # Dilate content
        dilation = cv2.dilate(edged, kernel, iterations=1)

        # Find contours
        contours = cv2.findContours(dilation.copy(),
                                    cv2.RETR_TREE,
                                    cv2.CHAIN_APPROX_SIMPLE)[0]

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

            # Resize
            resized = cv2.resize(dilation[y: y + h, x: x + w], (50, 50))

            # Digitalize
            threshold = cv2.threshold(resized, 127, 255, 0)[1]

            # Save as png
            image_name = "{}/{}-{}.png".format(SAVE_PATH,
                                               str(img_index).zfill(4),
                                               char_index)
            cv2.imwrite(image_name, threshold)


if __name__ == '__main__':
    main()