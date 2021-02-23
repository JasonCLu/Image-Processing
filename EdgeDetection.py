'''
Sobel Edge Detection
Laplacian Edge Detection
Canny Edge Detection
'''
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

# loading image
img0 = cv2.imread(imageFile)
#img0 = cv2.imread('/Users/jasonlu/Downloads/road_2.jpg')

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)

# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y


plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


plt.show()