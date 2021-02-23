import cv2
import numpy as np
import matplotlib.pyplot as plt

from tkinter import filedialog as fd
from tkinter import Tk

def GetFile():
	Tk().withdraw()
	return fd.askopenfilename()

# Get file
imageFile = GetFile()
print(imageFile)

# read image from file
bgr_img = cv2.imread(imageFile)

# convert image to grayscale
gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

# write/save new grayscale image
cv2.imwrite('grayscale.jpg',gray_img)

# display image
plt.imshow(gray_img, cmap = plt.get_cmap('gray'))
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
