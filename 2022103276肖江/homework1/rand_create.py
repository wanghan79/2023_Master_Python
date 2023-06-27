"""
平时作业1：
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1.	采用关键字参数作为随机数据结构及数量的输入；
2.	在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3.	其中随机数涵盖int，float和str三种类型。
"""

import random
import numpy as np


# 生成一个指定长度的随机字符串
def generateRandomStr(randomLength=26):
    randomStr = ''
    baseStr = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    baseStrLength = len(baseStr) - 1
    for _ in range(randomLength):
        randomStr += baseStr[random.randint(0, baseStrLength)]
    return randomStr


def dataSampling(**kwargs):
    count, shape, allDataType, strLength = kwargs['count'], kwargs[
        'shape'], kwargs['allDataType'], kwargs['strLength']
    floatData, intData, stringData = [], [], []

    for datatype in allDataType:
        for _ in range(0, count):
            if datatype == 'float':
                floatData.append(np.random.uniform(0, 10, shape))
            elif datatype == 'int':
                intData.append(np.random.randint(0, 10, shape))
            elif datatype == 'str':
                stringData.append(generateRandomStr(strLength))

    return floatData, intData, stringData


result = dataSampling(count=2, shape=(2, 2, 5), allDataType=[
                      'int', 'float', 'str'], strLength=26)
print(result)
