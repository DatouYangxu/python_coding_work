def cloestUAV(O,X,r):
    L=[]
    for i in O:
        L_=[i[0],'-']
        rmax=r
        for j in X:
            juli=((i[1]-j[1])**2+(i[2]-j[2])**2)**0.5
            if juli <=rmax and juli <=r:
                rmax=juli
                L_[1]=j[0]
        L.append(L_)
    result=L
    return result