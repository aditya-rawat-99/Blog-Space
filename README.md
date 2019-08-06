# Welcome to my mini blog

In this mini blog series I post things related to computer vision, more precisely what I learn along the way as I study computer vision.

Today we will learn about the `Hue`, `Saturation` and `value` (HSV) parameters of an image, what they mean and how to manipulate them.

Let's get started

# What is HSV?

Well, like RBG, HSV is also a color model that can sometimes be used in place of RBG values. For example, when you increase the brightness of an image (which we will do in a moment) you are actually maipulating the `value` parameter, or when you want to increase the intensity of a particular color in an image you change the `saturation` value.

So, to keep this mini blog "mini", let's dive into code

*prerequisite: You need to have __python__[https://www.python.org/] installed along with __OpenCV__[https://opencv.org/] and __numpy__[https://numpy.org/]*

First we will import the necessary libraries

```
import numpy as np
import cv2
```
