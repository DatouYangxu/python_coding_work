# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 08:49:50 2026

@author: 25688
"""

def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
n=int(input())
print(fac(n))