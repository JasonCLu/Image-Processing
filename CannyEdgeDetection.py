# The ultimate edge detection algorithm
# Steps:
# 1) Noice Reduction - 5x5 Gaussian filter
# 2) Calculate gradients (intensity gradients of image)
# 3) Nonmaximum suppression - upper threshold
# 4) Thresholding with hysterysis - upper/lower threshold
#

import cv2
import numpy as np
from matplotlib import pyplot as plt

from tkinter import filedialog as fd
from tkinter import Tk

def GetFile():
	Tk().withdraw()
	return fd.askopenfilename()

# Get file
imageFile = GetFile()
print(imageFile)

img = cv2.imread(imageFile,0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()