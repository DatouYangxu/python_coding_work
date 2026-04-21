# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 15:07:57 2025

@author: 25688
"""

"""
通过比较，找到最小值或最大值
"""

L=[2,3,4,7,9,1,2.9,12]
L_min=L[0]
for i in L:
    if i<=L_min:
        L_min=i
print(f'最小值是{L_min}')
#----------------------#

L=[2,3,4,7,9,1,2.9,12]
L_max=L[0]
for j in L:
    if j>=L_max:
        L_max=j
print(f'最大值是{L_max}')