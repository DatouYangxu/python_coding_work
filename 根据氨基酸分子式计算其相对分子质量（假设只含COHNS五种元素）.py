
def molecularWeight(protein):
    atom={'O':16,'C':12,'H':1,'N':14,'S':32}
    shu=[str(i) for i in range(10)]
    sum=0
    for i in range(len(protein)):
        if 'A'<=protein[i]<='Z':
            if i== len(protein)-1:
                sum=sum+atom[protein[i]]
            else:
                if protein[i+1] not in shu:
                    sum=sum+atom[protein[i]]
                else:
                    s_tr=''
                    for j in protein[i+1:]:
                        if j in shu:
                            s_tr=s_tr+j
                        else:
                            break
                    sum+=atom[protein[i]]*int(s_tr)
    return sum

formula = input()  #分子式
weight  = molecularWeight(formula)   #分子量
print('%s的分子量是：%d'%(formula, weight))
