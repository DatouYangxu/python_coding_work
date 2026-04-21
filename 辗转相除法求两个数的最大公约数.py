# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 21:09:31 2025

@author: 25688
"""

#"找最大公约数"
a,b=eval(input('输入：',)),eval(input('输入：',))
c=a%b
while c != 0:
    a,b=b,c
    c=a%b
print(b)  #b即为最大公约数