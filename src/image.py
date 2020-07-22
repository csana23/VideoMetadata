import cv2
import numpy as np
from collections import namedtuple

#brange brightness range
#bval brightness value
BLevel = namedtuple("BLevel", ['brange', 'bval'])

#all possible levels
_blevels = [
    BLevel(brange=range(0, 24), bval=0),
    BLevel(brange=range(23, 47), bval=1),
    BLevel(brange=range(46, 70), bval=2),
    BLevel(brange=range(69, 93), bval=3),
    BLevel(brange=range(92, 116), bval=4),
    BLevel(brange=range(115, 140), bval=5),
    BLevel(brange=range(139, 163), bval=6),
    BLevel(brange=range(162, 186), bval=7),
    BLevel(brange=range(185, 209), bval=8),
    BLevel(brange=range(208, 232), bval=9),
    BLevel(brange=range(231, 256), bval=10),
]


def detect_level(h_val):
    h_val = int(h_val)
    for blevel in _blevels:
        if h_val in blevel.brange:
            return blevel.bval
    raise ValueError("Brightness Level Out of Range")


def get_img_avg_brightness(image_file_path):
    img = cv2.imread(image_file_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # display converted image
    cv2.imshow('hsv_image', hsv) 
    cv2.waitKey(0)

    # v, value = brightness
    hue, saturation, v = cv2.split(hsv)

    return int(np.average(v.flatten()))

brightness = get_img_avg_brightness('C:/Users/richa/Pictures/sad_cat.jpg')
level = detect_level(brightness)

print('Level of average brightness of image:', level)

