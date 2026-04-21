# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 20:34:51 2025

@author: 25688
"""

def oula(n):
    t=n**2+n+41
    return t
def sushu(n):
    '判断是否是素数,并且计算出相应的因数'
    L=[]
    s=True
    for i in range(1,n+1):
        if n%i == 0:
            L.append(i)
    if len(L) == 2:
        s = True
    else:
        s = False
    return s

i=True
j=1
while i==True:
    i=sushu(oula(j))
    if i:
        print('f(%d)=%d是素数'%(j,oula(j)))
    else:
        break
    j+=1

L=[]
for s in range(2,oula(j)):
    if oula(j)%s == 0:
        L.append(s)
        break
a,b=L[0],oula(j)/L[0]
print('f(%d)=%d=%d*%d不是素数'%(j,oula(j),a,b))

