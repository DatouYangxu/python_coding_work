# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:43:03 2026

@author: 25688
"""

def spn(n):
    if n//10==0:
        print(n)
        return None
    else:
        spn(n//10)#递归调用，逐层深入
        print(n%10)#调用后，后面的语句在返回时再执行
print(spn(1234))