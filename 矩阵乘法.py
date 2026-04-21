# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 20:56:50 2025

@author: 25688
"""

def multiply(A,B):
    m,p,n=len(A),len(A[0]),len(B[0])
    C=[[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for t in range(p):
                C[i][j]=A[i][t]*B[t][j]+C[i][j]
    return C