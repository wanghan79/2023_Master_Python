from random import random
def dataSampling(datatype,datarange,num,string=8):
    res=set()
    for i in range(0,num):
        if datatype is int:
            item=random.randint(1,10)
            res.add(item)
            continue
        elif datatype is float:

            item=random.uniform(10,100)

            res.add(item)
            continue
        else:
            continue

    return res

if __name__ == '__main__':
    dataSampling(float,10,10)

