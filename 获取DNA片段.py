def getDNA(sdna):
    result=[]
    i=0
    while i < len(sdna)-2 :
        if sdna[i:i+3]!='ATG':
            i+=1
            continue 
        start=i+3
        j=start
        while j<len(sdna)-2:
            triplet=sdna[j:j+3]
            if triplet in ['TAG','TAA','TGA']:
                gene = sdna[start:j]
                if gene and all(tri not in gene for tri in ['ATG','TAG','TAA','TGA']):
                    result.append(gene)
                i=j+3
                break
            j+=1
        else:
            i+=1
            continue 
    return result if result else "no gene is found"