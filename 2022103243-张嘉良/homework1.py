"""
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1. 采用关键字参数作为随机数据结构及数量的输入；
2. 在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3. 其中随机数涵盖int，float和str三种类型。
"""

import random

def dataSampling(**kwargs):
    result = []
    for datatype, datarange in kwargs.items():
        if datatype == 'int':
            result.append(random.randint(*datarange))
        elif datatype == 'float':
            result.append(random.uniform(*datarange))
        elif datatype == 'str':
            length = random.randint(*datarange)
            result.append(''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length)))
    return result

# 调用示例
# result = dataSampling(int=(1, 100), float=(0, 1), str=(5, 10))
# print(result)
