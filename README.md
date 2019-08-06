# Welcome to my mini blog

In this mini blog series I post things related to computer vision, more precisely what I learn along the way as I study computer vision.

Today we will learn about the `Hue`, `Saturation` and `value` (HSV) parameters of an image, what they mean and how to manipulate them.

Let's get started

# What is HSV?

Well, like RBG, HSV is also a color model that can sometimes be used in place of RBG values. For example, when you increase the brightness of an image (which we will do in a moment) you are actually maipulating the `value` parameter, or when you want to increase the intensity of a particular color in an image you change the `saturation` value.

So, to keep this mini blog "mini", let's dive into code

*prerequisite: You need to have [python](https://www.python.org/) installed along with [OpenCV](https://opencv.org/) and [numpy](https://numpy.org/)*

First we will import the necessary libraries

```
import numpy as np
import cv2
```

Then we need an image to work on.

I pulled [this](https://d17fnq9dkz9hgj.cloudfront.net/uploads/2018/04/Beagle_02.jpg) of dog (because I love dogs).

Next, we will load the image and show the result (to quit press any key on the keyboard)

```
img = cv2.imread("/home/aditya/Downloads/Beagle.jpg")
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

Next, we will convert the img to HSV and create a function that will change the value of, well `value`.

```
# This function helps us to show the image without needing to write 3 lines of code every time

def showImage(img,name):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def increase_intensity(hsv, value = 10):
    h,s,v = cv2.split(hsv)
    
    v[v <=200] = value
    final_hsv = cv2.merge((h,s,v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img
    
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```
Let's see how the image looks

```
img = increase_intensity(hsv)
showImage(img, "img")
```
![TestImage](https://raw.githubusercontent.com/aditya-rawat-99/Blog-Space/master/Beagle2.jpg)
