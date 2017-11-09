# -*- coding: utf-8 -*-

"""

Created on Thu Oct 12 10:21:34 2017



@author: tianzixie

"""



import numpy as np

from PIL import Image

#I = Image.open( "C://Users/tianzixie/Desktop/181079.jpg")
imgsrc = "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300/html/images/plain/normal/gray/181079.jpg"
from skimage import io
I = io.imread(imgsrc)

imgArr = np.array(I)

imgArrr=np.array(I)

#import image to array

#Image.fromarray(imgArr).show()

a=50

b=150

c=2

for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        x=imgArr[i,j]

        if x>=0 and x<a:

            imgArrr[i,j]=0   

        if x>=a and x<b:

            imgArrr[i,j]=c*(x-a)

        if x>b and x<256:

            imgArrr[i,j]=c*(b-a)

#calculate

tempImg = Image.fromarray(imgArrr)

#turn array to image
tempImg.show()
#tempImg.save("C://Users/tianzixie/Desktop/181079,a=50,b=150,c=2.jpg")

#Image.fromarray(imgArrr).show()