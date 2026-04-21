# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 20:11:00 2025

@author: 25688
"""
def add(a,b):
    if '/' in a and '/'in b:
        a_fenmu,b_fenmu=int(a[a.index('/')+1:]),int(b[b.index('/')+1:])
        if a_fenmu == b_fenmu:
            fenzi=int(a[:a.index('/')])+int(b[:b.index('/')])
            fenmu=a_fenmu
        else:
            fenmu=a_fenmu*b_fenmu
            fenzi=int(a[:a.index('/')])*b_fenmu+int(b[:b.index('/')])*a_fenmu
        if fenzi%fenmu==0:
            jieguo=str(fenzi//fenmu)
        else:
            yueshu=max(abs(fenzi),fenmu)
            for i in range(yueshu):
                if fenzi%(yueshu-i)==0 and fenmu%(yueshu-i)==0:
                    yueshu=yueshu-i
                    break
            fenzi,fenmu=fenzi//yueshu,fenmu//yueshu
            fenshu=(str(fenzi),'/',str(fenmu))
            jieguo=''.join(fenshu)
    else:
        if ('/'not in a) and ('/'in b):
            fenmu=int(b[b.index('/')+1:])
            fenzi=int(a)*fenmu+int(b[:b.index('/')])
            fenshu=(str(fenzi),'/',str(fenmu))
            jieguo=''.join(fenshu)
        else:
            if ('/'in a)and ('/'not in b):
                fenmu=int(a[a.index('/')+1:])
                fenzi=int(b)*fenmu+int(a[:a.index('/')])
                fenshu=(str(fenzi),'/',str(fenmu))
                jieguo=''.join(fenshu)
            else:
                fenshu=int(a)+int(b)
                jieguo=str(fenshu)
    return jieguo
x = input()
y = input()
z = add(x, y) #分数相加
print('%s + %s = %s' % (x, y, z))