# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 20:44:43 2025

@author: 25688
"""

# 有abc三个整数，不妨令a<b<c,
# ruo b|a,jiuling c%a,zai c yu a zhijian xunzhao gongyueshu
# ruo b|/a,jiuzai b yu a zhi jian xun zhao gong yue shu
a = int(input('输入'))
b = int(input('输入'))
c = int(input('输入'))
L=[a,b,c]
L.sort()
l1,l2,l3=L[0],L[1],L[2]
if l2%l1==0:
    d=l3%l1
    while d!=0:
        l3=l1
        l1=d
        d=l3%l1
    print(l1)
else:
    e=l2%l1
    while e!=0:
        l2=l1
        l1=e
        e=l2%l1
    print(l1)
    # 如果b能整除a，那么最大公约数是a的一个因数；
    # 接下来只需求a与c的最大公约数
    # 如果b不能整除a，那么最大公约数存在于a与b的因数之间，
    # 就去求b与a的最大公约数
    # 然后求该公约数与c的最大公约数