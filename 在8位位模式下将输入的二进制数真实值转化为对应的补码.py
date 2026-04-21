# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 20:56:36 2025

@author: 25688
"""

def ZhenToYuan(z):
    Yuan='1' if '-'in str(z) else '0'
    z_shuzhi=z[:] if str(z)[0] not in ['-','+'] else str(z)[1:]
    
    yuanma=(Yuan,'0'*(7-len(z_shuzhi)),z_shuzhi)
    return ''.join(yuanma)

def YuanToFan(y):
    if y[0]=='0':
        fanma=y
    else:
        fanma='1'
        for i in range(1,len(y)):
            if y[i] == '1':
                fanma=fanma+'0'
            else:
                fanma=fanma+'1'
    return fanma

def ZhenToBu(r):
    Yuan=ZhenToYuan(r)
    if Yuan[0]=='0':
        Bu=Yuan
    else:
        fanma=YuanToFan(Yuan)
        if '0' not in fanma:
            Bu='0'*8
        else:
            fanma_list=list(fanma)
            fanma_list.reverse()
            iD=fanma_list.index('0')
            L=fanma_list[iD+1:]
            L.reverse()
            bu=''.join(L)
            buma=(bu,'1','0'*(7-len(bu)))
            Bu=''.join(buma)
            
    return Bu        


z = input()       #真实值
b = ZhenToBu(z)   #转换成8位补码
print('%s -> %s' % (z, b))