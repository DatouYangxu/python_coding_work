# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 20:14:12 2025

@author: 25688
"""

def sushu(n):
    L=[]
    for i in range(1,n):
        if n%i==0:
            L.append(i)
    if len(L)==1:
        return str(L[0])
    else:
        return L[1],n//L[1]
i=1
while True:
    n=i**2+i+41
    if len(sushu(n))==1:
        print('f(%d)=%d是素数'%(i,n))
    else:
        a,b=sushu(n)
        print('f(%d)=%d=%d*%d不是素数'%(i,n,a,b))
        break
    i=i+1
    