# -*- coding: utf-8 -*-

"""

Created on Thu Oct 12 11:09:22 2017



@author: tianzixie

"""





#from numpy import *

#from sympy import E

#import matplotlib.image as mpimg





import math

import numpy as np

from PIL import Image


I = Image.open( "..//images/181079.jpg")
#I = Image.open( "C://Users/tianzixie/Desktop/181079.jpg")
#imgsrc = "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300/html/images/plain/normal/gray/181079.jpg"
#from skimage import io
#I = io.imread(imgsrc)
#import image from a url
#Image.fromarray(I).show()
imgArr = np.array(I)

imgArrr=np.array(I)

#import image to array



for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        x=imgArr[i,j]

        y=1*math.log10(1+x)

        imgArrr[i,j]=y

#calculate

tempImg = Image.fromarray(imgArrr)

#turn array to image

tempImg.show()
#tempImg.save("C://Users/tianzixie/Desktop/181079,1.jpg")
#
##save image with c=1

#Image.fromarray(imgArr).show()

for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        x=imgArr[i,j]

        y=10*math.log10(1+x)

        imgArrr[i,j]=y

tempImg = Image.fromarray(imgArrr)
tempImg.show()
#tempImg.save("C://Users/tianzixie/Desktop/181079,10.jpg")

#save image with c=10



for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        x=imgArr[i,j]

        y=100*math.log10(1+x)

        imgArrr[i,j]=y

tempImg = Image.fromarray(imgArrr)
tempImg.show()
#tempImg.save("C://Users/tianzixie/Desktop/181079,100.jpg")

#save image with c=100



for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        x=imgArr[i,j]

        y=1000*math.log10(1+x)

        imgArrr[i,j]=y

tempImg = Image.fromarray(imgArrr)
tempImg.show()
#tempImg.save("C://Users/tianzixie/Desktop/181079,1000.jpg")

#save image with c=1000



# c should be within a suitable range, or the result would be too ugly