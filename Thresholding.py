'''
Simplest method of image segmentation
Values above a threshold is set to one value (e.g. White)
Values below a threshold is set to another value (e.g. Black)

cv2.threshold(src, thresh, maxval, type, [dst])
 
src    - input array (single-channel, 8-bit or 32-bit floating point). This is the source image, which should be a grayscale image.
thresh - threshold value, and it is used to classify the pixel values.
maxval - maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types. It represents the value to be given if pixel value is more than (sometimes less than) the threshold value.
type   - thresholding type.(see threshold for details).
		cv2.THRESH_BINARY
		cv2.THRESH_BINARY_INVY
		cv2.THRESH_TRUNCY
		cv2.THRESH_TOZEROY
		cv2.THRESH_TOZERO_INVY
dst    - output array of the same size and type as src.
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/gradient.png',0)
#img = cv2.imread('images/gradient.png',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
