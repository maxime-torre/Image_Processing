"""
Created on Tue Apr 16/11/2022

@author: Maxime Torre
"""
from re import I
import scipy
import numpy as np
import skimage.io as skio
from os.path import join
import scipy.ndimage as scnd
import skimage.filters as skf
from skimage import color
from skimage import filters

import skimage as sk
import skimage.color as skc
import skimage.data as skd
import matplotlib.pyplot as plt
from skimage import util 
from skimage.util import crop

## 1 - Image sketching -------------------------------------------------------------------------------------------

filename = r'jacob_collier.jpg'
dirpath = r'/TP_traitement_image' 
filepath = join(dirpath, filename)
print(filepath)

img = skio.imread(filepath)
grayscale = color.rgb2gray(img)
inverted_img = util.invert(grayscale)

print("le type de mon image est :",inverted_img.dtype)
# float -> [0-1] et uint -> [0-255]
print(img.shape[0])
print(img.shape[1])

img_gaussian_10 = scipy.ndimage.gaussian_filter(inverted_img,10)
img_gaussian_5 = scipy.ndimage.gaussian_filter(inverted_img,5)
img_gaussian_05 = scipy.ndimage.gaussian_filter(inverted_img,0.5)

sketch_10 = (img_gaussian_10)/inverted_img 
sketch_5 = (img_gaussian_5)/inverted_img 
sketch_05 = (img_gaussian_05)/inverted_img 

for i in range(img.shape[0]):
    for k in range(img.shape[1]):
        if sketch_10[i][k] > 1:
            sketch_10[i][k] = 1

for i in range(img.shape[0]):
    for k in range(img.shape[1]):
        if sketch_5[i][k] > 1:
            sketch_5[i][k] = 1

for i in range(img.shape[0]):
    for k in range(img.shape[1]):
        if sketch_05[i][k] > 1:
            sketch_05[i][k] = 1

f, axarr = plt.subplots(2,2)

print("Loaded image has dimensions:", img.shape)
axarr[0,0].imshow(img)
axarr[0,0].set_title("Image Based")
axarr[0,1].imshow(sketch_05, cmap=plt.cm.gray)
axarr[0,1].set_title("Sigma = 0.5")
axarr[1,0].imshow(sketch_5, cmap=plt.cm.gray)
axarr[1,0].set_title("Sigma = 5")
axarr[1,1].imshow(sketch_10, cmap=plt.cm.gray)
axarr[1,1].set_title("Sigma = 10")


plt.show()