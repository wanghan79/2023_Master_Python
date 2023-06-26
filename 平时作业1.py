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
result = dataSampling(int=(1, 100), float=(0, 1), str=(5, 10))
print(result)
