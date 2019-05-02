# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:22:23 2019

@author: s140121038
"""

def normalize(x):
    x[0]=1 #for the normalize, the leading edge x point must equal 1
    x[len(x)-1]=1 #for the normalize, the trailing edge x point must equal 1
    return x
normalize(x)