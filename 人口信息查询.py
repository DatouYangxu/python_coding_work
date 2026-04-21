"""
人口信息查询
"""
filename=r'my_python_code\exam.txt'
def getinfo(shengName):
    sheng={}
    with open(filename,'r') as fil:
        for i in fil:
            if i.strip():
                line=i.strip().split()
                if len(line) == 1:
                    current_province=line[0]
                    sheng[current_province]=[]
                elif len(line) == 2:
                    if current_province:
                        chengshi=line[0]
                        renkou=int(line[1])
                        sheng[current_province].append((chengshi,renkou))
    max_chengshi=max(sheng[shengName],key=lambda x: x[1])
    city=max_chengshi[0]
    population=max_chengshi[1]
    return city,population
