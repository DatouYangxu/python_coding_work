# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 22:40:40 2026

@author: 25688
"""

import matplotlib.pyplot as plt
import numpy as np
seq=np.array(range(1,9))
ddct={'d1':'','d2':'','d3':'','d4':'','d5':'','d6':'','d7':'','d8':'','d9':'','d10':'','d11':'','d12':''}
flag=['-1','-2','-3','-4','-s','-p','-*','-+','-D','-d','-H','-h']
ct,step=0,10
keys=list(ddct.keys())
while ct < 12:
    ddct[keys[ct]]=[step for i in seq]
    a=np.array(ddct[keys[ct]])
    plt.plot(seq,a,flag[ct])
    step=step+10
    ct=ct+1
plt.show()
