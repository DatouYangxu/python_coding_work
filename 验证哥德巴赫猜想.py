# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:55:18 2025

@author: 25688
"""

def Goldbach(n):
    for i in range(2,n):
        L=[]
        for j in range(1,i+1):
            if i%j == 0:
                L.append(j)
            else:
                continue
        if len(L) != 2:
            continue
        else:
            n1=i
            n2=n-i
            L1=[]
            for a in range(1,n2+1):
                if n2%a == 0:
                    L1.append(a)
                else:
                    continue
            if len(L1) != 2:
                continue
            else:
                break
    L2=[n1,n2]
    L2.sort()
    return L2[0],L2[1]

N=int(input(''))
N1,N2 = Goldbach(N)
print('%d = %d + %d' % (N, N1, N2))
