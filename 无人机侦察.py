# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 14:54:08 2025

@author: 25688
"""

def cav(O,X,r):
    result=[]
    for xx in X:
        d_min=r
        result_zi=[xx[0],'-']
        for oo in O:
            d=((xx[1]-oo[1])**2+(xx[2]-oo[2])**2)**0.5
            result_zi=[]
            if d<=r and d<=d_min:
                d_min=d
                result_zi=[xx[0],oo[0]]
        result.append(result_zi)
    return result