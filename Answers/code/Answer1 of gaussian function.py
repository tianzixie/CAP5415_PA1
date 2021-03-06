#!/usr/bin/env python2

# -*- coding: utf-8 -*-

"""

Created on Thu Oct 12 18:47:30 2017



@author: tianzixie

"""

import numpy as np

import math



def gaussian(sigma,ksize):

    array=np.zeros(ksize)

    c=0

    for x in range (ksize):

        ya=(x-int(ksize/2))*(x-int(ksize/2))

        yb=sigma*sigma

        y=(float)(ya)/(float)(yb)

        ex=math.exp(-y)        

        array[x]=ex

        c=sum(array)        

    for x in range(ksize):

        array[x]=array[x]/c        

    return array

    #get gaussian mask of 1 dimension



    

print (gaussian(1,3))

#print gaussian mask when sigma=1 and size=3