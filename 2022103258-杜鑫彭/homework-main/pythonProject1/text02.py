import random
from typing import List, Tuple, Set
from functools import wraps

# 定义装饰器，实现机器学习方法和验证指标操作的任意组合
def machine_learning(*args):
    def wrapper(func):
        @wraps(func)
        def inner(*args1, **kwargs):
            print('Machine learning method:', args)
            result = func(*args1, **kwargs)
            return result
        return inner
    return wrapper

def validation_metrics(*args):
    def wrapper(func):
        @wraps(func)
        def inner(*args1, **kwargs):
            result = func(*args1, **kwargs)
            print('Validation metrics:', args)
            return result
        return inner
    return wrapper

# 数据采样函数
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

# 使用装饰器修饰数据采样函数
@machine_learning('SVM', 'CNN')
@validation_metrics('ACC', 'MCC')
def generate_random_data():
    int_data = {'int': [1, 100]}
    float_data = {'float': [-10.0, 10.0]}
    str_data = {'str': 'abcdefghijklmnopqrstuvwxyz'}
    print(dataSampling(**int_data))
    print(dataSampling(**float_data))
    print(dataSampling(**str_data))
    print(dataSampling(**int_data, **float_data, **str_data))

# 调用示例
if __name__ == '__main__':
    generate_random_data()