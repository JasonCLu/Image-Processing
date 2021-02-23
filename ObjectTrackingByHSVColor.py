'''
HSV, unlike RGB, separates the image intensity (lima), from the color information (chroma). 
This can be very useful if we want to focused on the intensity component, and leave the color components alone. 

Actually, in computer vision, we sometimes want to separate color components from intensity for various reasons, 
such as robustness to lighting changes, or removing shadows. 

HSV colorspace has the lighting intensity information removed. 
'''

# capture.py
import numpy as np
import cv2

# Capture video from camera
# cap = cv2.VideoCapture(0)

# Capture video from file
cap = cv2.VideoCapture('videos/BlueUmbrella.webm')

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    # Tracking Blue Object:
    #	1) Convert frame from BGR to HSV color-space.
    #	2) Threshold the HSV image for a range of blue color.
    #	3) Extract the blue object alone
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image in order to Extract the blue only
    res = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()