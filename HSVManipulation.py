# Import all the necessary libraries

import numpy as np
import cv2

"""Method to manipulate the Value"""
def increase_intensity(hsv, value = 10):
    h,s,v = cv2.split(hsv)
    
    v[v <=200] = value
    final_hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

"""Method to show Image"""
def showImage(img,name):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    

# Load the Image
img = cv2.imread("/home/aditya/Downloads/Beagle.jpg")

# Convert it to HSV 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Change the Value
img = increase_intensity(hsv)

# Show imaage
showImage(img, "img")
