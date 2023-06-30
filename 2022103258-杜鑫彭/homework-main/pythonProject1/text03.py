import random
from typing import List, Tuple, Set
from abc import ABC, abstractmethod


# 抽象类，定义接口
class DataGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


# 实现具体类
class RandomDataGenerator(DataGenerator):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def generate(self):
        result = []
        for data_type, data_range in self.kwargs.items():
            if data_type == 'int':
                result.append(random.randint(*data_range))
            elif data_type == 'float':
                result.append(random.uniform(*data_range))
            elif data_type == 'str':
                result.append(''.join(random.sample(data_range, 5)))
            else:
                raise ValueError('Invalid data type')
        return result


# 定义装饰器，实现机器学习方法和验证指标操作的任意组合
def machine_learning(*args):
    def wrapper(cls):
        @wraps(cls)
        def inner(*args1, **kwargs):
            print('Machine learning method:', args)
            instance = cls(*args1, **kwargs)
            result = instance.generate()
            return result

        return inner

    return wrapper


def validation_metrics(*args):
    def wrapper(cls):
        @wraps(cls)
        def inner(*args1, **kwargs):
            instance = cls(*args1, **kwargs)
            result = instance.generate()
            print('Validation metrics:', args)
            return result

        return inner

    return wrapper


# 使用装饰器修饰具体类
@machine_learning('SVM', 'CNN')
@validation_metrics('ACC', 'MCC')
class RandomData:
    def __init__(self, **kwargs):
        self.generator = RandomDataGenerator(**kwargs)

    def generate(self):
        return self.generator.generate()


# 调用示例
if __name__ == '__main__':
    int_data = {'int': [1, 100]}
    float_data = {'float': [-10.0, 10.0]}
    str_data = {'str': 'abcdefghijklmnopqrstuvwxyz'}
    data = RandomData(**int_data, **float_data, **str_data)
    print(data.generate())