import numpy as np
import random
import string
'''
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1.	采用关键字参数作为随机数据结构及数量的输入；
2.	在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3.	其中随机数涵盖int，float和str三种类型。
'''

def dataSampling(**kwargs):
    # data用于存储生成数据
    data = []
    shape = None
    if 'shape' in kwargs:
        shape = kwargs['shape']
    for key, value in kwargs.items():
        if key == 'int':
            for i in range(value):
                data.append(random.randint(0, 100))
            if shape != None:
                data = np.array(data)
                data.resize(shape)
        elif key == 'float':
            for i in range(value):
                data.append(random.uniform(0, 1))
            if shape != None:
                data = np.array(data)
                data.resize(shape)
        elif key == 'str':
            for i in range(value):
                data.append(''.join(random.sample(string.ascii_letters + string.digits, random.randint(1, 10))))
    return data

# 进行测试
# print(dataSampling(int=7))
# print(dataSampling(int=6, shape=(2,3)))
# print(dataSampling(float=8, shape=(8,1)))
# print(dataSampling(str=4))
# print(dataSampling(int=3, float=4, str=5))
