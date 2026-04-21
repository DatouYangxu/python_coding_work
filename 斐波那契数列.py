# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:06:35 2026

@author: 25688
"""

f0,f1=1,1
def febonaci(n):
    if n==0 or n==1:
        return 1
    else:
        return febonaci(n-1)+febonaci(n-2)
# n=int(input())
# print(febonaci(n))
for i in range(16):
    print(f"斐波那契数列的第{i}项为：{febonaci(i)}")