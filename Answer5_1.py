# -*- coding: utf-8 -*-

"""

Spyder Editor



This is a temporary script file.

"""

import numpy as np

import pylab as plt

from PIL import Image

import math

#I = Image.open( "C://Users/tianzixie/Desktop/1610621.jpg")
imgsrc = "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300/html/images/plain/normal/gray/161062.jpg"
from skimage import io
I = io.imread(imgsrc)

imgArr = np.array(I)

imgArrr=np.array(I)

Image.fromarray(imgArr).show()

his = np.zeros(256)

prob = np.zeros(256)

#create array

for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        his[imgArr[i, j]] = his[imgArr[i, j]] + 1

for i in range(256):

    prob[i]=his[i]/(imgArr.shape[0]*imgArr.shape[1])

plt.plot(prob)

plt.show()

#show a picture of probability before operation

plt.plot(his)

plt.show()

#show a histogram before operation

E=0

C=0

for j in range(256):

    A=0

    B=0

    

    for i in range(j):

        if prob[i]>0:

            A=A-prob[i]*math.log(prob[i])

    for i in range(256-j):

        if prob[i]>0:

            B=B-prob[i]*math.log(prob[i])

    if C<(A+B):

        C=A+B

        D=j

cu=np.zeros(256)

for i in range(256):

    if i==0:

        cu[i]=prob[i]*255

    else:

         cu[i]=cu[i-1]+prob[i]*255   

P=0

for i in range(imgArrr.shape[0]):

        for j in range(imgArrr.shape[1]):

            a= cu[imgArrr[i,j]]+0.5            

            imgArrr[i,j]=int(a)

#operation

Image.fromarray(imgArrr).show() 

his2 = np.zeros(256)

prob = np.zeros(256) 

for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        his2[imgArrr[i, j]] = his2[imgArrr[i, j]] + 1    

for i in range(256):

    prob[i]=his2[i]/(imgArr.shape[0]*imgArr.shape[1])

plt.plot(prob)

plt.show()

#show a picture of probability after operation

plt.plot(his2)

plt.show()

#show a histogram after operation
