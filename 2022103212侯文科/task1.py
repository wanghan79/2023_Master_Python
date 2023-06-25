import random

def randomInt(datarange,num):
    result=set()
    for index in range(0,num):
        it=iter(datarange)
        item=random.randint(next(it),next(it))
        result.add(item)
    return  result

def randomFloat(datarange,num):
    result=set()
    for index in range(0,num):
        it=iter(datarange)
        item=random.uniform(next(it),next(it))
        result.add(item)
    return  result

def randomStr(datarange,strlength):
    result=set()
    item=''.join(random.SystemRandom().choice(datarange) for _ in range(strlength))
    result.add(item)
    return  result

def task1_run(**kwargs):
    result_1=randomInt([2,100],10)
    result_2=randomFloat([11.2,15.6],10)
    result_3=randomStr(['a','z'],10)
    print("随机整形：")
    print(result_1)
    print("随机字符型：")
    print(result_2)
    print("随机字符型：")
    print(result_3)