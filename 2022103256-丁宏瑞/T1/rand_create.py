"""
平时作业1：
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1.	采用关键字参数作为随机数据结构及数量的输入；
2.	在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3.	其中随机数涵盖int，float和str三种类型。
"""
import random
import numpy as np
import string

def dataSampling(**kwargs):
    len = kwargs['len']
    shape = kwargs['shape']
    desire_type = kwargs['desire_type']
    str_length = kwargs['str_length']

    float_data = []
    int_data = []
    string_data = []
    for datatype in desire_type:
        for _ in range(0, len):
            if datatype == 'float':
                float_data.append(np.random.uniform(0, 10, shape))
            elif datatype == 'int':
                int_data.append(np.random.randint(0, 10, shape))
            elif datatype == 'str':
                item = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_length))
                string_data.append(item)
    return float_data ,int_data, string_data


'''生成2组随机整数和2组字符串，随机整数形状为(2,2,5)，字符串长度为26'''
result = dataSampling(len=2, shape=(2, 2, 5), desire_type=['int', 'str'], str_length=26)
print(result)
