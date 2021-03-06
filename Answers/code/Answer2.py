# -*- coding: utf-8 -*-

"""

Spyder Editor



This is a temporary script file.

"""







import numpy as np

import pylab as plt

from PIL import Image

import math
I = Image.open( "..//images/232038.jpg")
#I = Image.open( "C://Users/tianzixie/Desktop/232038.jpg")
#imgsrc = "https://www2.eecs.berkeley.edu/Research/Projects/CS/vision/bsds/BSDS300/html/images/plain/normal/gray/232038.jpg"
#from skimage import io
#I = io.imread(imgsrc)

imgArr = np.array(I)

imgArrr=np.array(I)

Image.fromarray(imgArr).show()

his = np.zeros(256)

prob = np.zeros(256)

for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        his[imgArr[i, j]] = his[imgArr[i, j]] + 1

for i in range(256):

    prob[i]=his[i]/(imgArr.shape[0]*imgArr.shape[1])

plt.plot(prob)

plt.show()

#show picture of probability

plt.plot(his)

plt.show()

#shoe picture of histogram

E=0

C=0

for j in range(256):

    A=0

    B=0

    for i in range(j):

        if prob[i]!=0:

            A=A-prob[i]*math.log(prob[i])

    for i in range(256-j):

        if prob[i]!=0:

            B=B-prob[i]*math.log(prob[i])

    if C<(A+B):

        C=A+B

        D=j



#A=A-prob[i]*math.log(prob[i]) calculates maximum total entropy, so is B=B-prob[i]*math.log(prob[i])

#value of D corresponding to maximum total entropy

#maximum total entropy H(T)=H(A)+H(B) corresponding to C=A+B when the right D is found

for i in range(imgArr.shape[0]):

    for j in range(imgArr.shape[1]):

        if imgArr[i, j]<D:

            imgArr[i, j]=0

        else:

            imgArr[i, j]=255

Image.fromarray(imgArr).show() 