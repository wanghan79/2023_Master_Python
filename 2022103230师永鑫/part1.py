import random
import string
"""
实现随机数据结构生成封装函数dataSampling(**kwargs)，以及相应的调用示例，主要考察点是关键字参数的使用，具体要求如下：
1. 采用关键字参数作为随机数据结构及数量的输入；
2. 在不修改代码的前提下，根据kwargs定义内容实现任意数量、任意维度、一层深度的随机数据结构生成；
3. 其中随机数涵盖int，float和str三种类型。
"""
def dataSampling(length=1, dimension=1):
    result = []

    for _ in range(dimension):
        sample = []
        for _ in range(length):
            data_type = random.choice(['int', 'float', 'str'])
            if data_type == 'int':
                sample.append(random.randint(0, 100))
            elif data_type == 'float':
                sample.append(round(random.uniform(0, 1), 2))
            elif data_type == 'str':
                sample.append(''.join(random.choices(string.ascii_letters, k=5)))
        result.append(sample)

    return result


# 调用示例
random_data = dataSampling(length=10, dimension=5)

print(random_data)

def run():
    # 第一次作业的代码
    print("这是第一次作业")
