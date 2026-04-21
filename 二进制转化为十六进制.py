# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 16:20:29 2025

@author: 25688
"""

def BinToHex(n):
    
    L=[str(i) for i in str(n)]
    a=len(L)%4
    if a != 0:
        L1=['0']*(4-a)+L
    else:
        L1=L[:]
    
    b=len(L1)//4
    H=['A','B','C','D','E','F']
    h=[]
    for i in range(1,b+1):
        sum=0
        for j in range(4*(i-1),4*i):
            sum=sum+int(L1[j])*2**(4-(j-4*(i-1))-1)
        if sum >=10:
            sum=H[sum-10]
        h.append(sum)
    
    s=''
    for m in range(len(h)):
        s=s+str(h[m])
    return s

