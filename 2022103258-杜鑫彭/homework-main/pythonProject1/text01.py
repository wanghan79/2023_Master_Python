import random
from typing import List, Tuple, Set

def dataSampling(**kwargs):
    result = []
    for data_type, data_range in kwargs.items():
        if data_type == 'int':
            result.append(random.randint(*data_range))
        elif data_type == 'float':
            result.append(random.uniform(*data_range))
        elif data_type == 'str':
            result.append(''.join(random.sample(data_range, 5)))
        else:
            raise ValueError('Invalid data type')
    return result

# 调用示例
if __name__ == '__main__':
    int_data = {'int': [1, 100]}
    float_data = {'float': [-10.0, 10.0]}
    str_data = {'str': 'abcdefghijklmnopqrstuvwxyz'}
    print(dataSampling(**int_data))
    print(dataSampling(**float_data))
    print(dataSampling(**str_data))
    print(dataSampling(**int_data, **float_data, **str_data))