import random
from typing import List, Tuple, Set
from abc import ABC, abstractmethod
from functools import wraps


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

        return cls

    return wrapper


def validation_metrics(*args):
    def wrapper(cls):
        @wraps(cls)
        def inner(*args1, **kwargs):
            instance = cls(*args1, **kwargs)
            result = instance.generate()
            print('Validation metrics:', args)
            return result

        return cls

    return wrapper


# 使用装饰器修饰具体类
@machine_learning('SVM', 'CNN')
@validation_metrics('ACC', 'MCC')
class RandomData:
    def __init__(self, **kwargs):
        self.generator = RandomDataGenerator(**kwargs)

    def generate(self):
        return self.generator.generate()


# 控制台交互程序
def main():
    while True:
        print('请输入要运行的作业号（1、2或3），输入q退出程序：')
        job_number = input().strip()
        if job_number == 'q':
            break
        elif job_number == '1':
            int_data = {'int': [1, 100]}
            float_data = {'float': [-10.0, 10.0]}
            str_data = {'str': 'abcdefghijklmnopqrstuvwxyz'}
            print(RandomData(**int_data).generate())
            print(RandomData(**float_data).generate())
            print(RandomData(**str_data).generate())
            print(RandomData(**int_data, **float_data, **str_data).generate())
        elif job_number == '2':
            @machine_learning('LR', 'SVM')
            @validation_metrics('ACC', 'F1')
            class LogisticRegression:
                def __init__(self, input_dim, output_dim):
                    self.input_dim = input_dim
                    self.output_dim = output_dim

                def generate(self):
                    return f'Logistic regression model with input_dim={self.input_dim} and output_dim={self.output_dim}'

            @machine_learning('MLP', 'CNN')
            @validation_metrics('ACC', 'Precision')
            class MultiLayerPerceptron:
                def __init__(self, input_dim, output_dim, hidden_dim):
                    self.input_dim = input_dim
                    self.output_dim = output_dim
                    self.hidden_dim = hidden_dim

                def generate(self):
                    return f'Multi-layer perceptron model with input_dim={self.input_dim}, output_dim={self.output_dim} and hidden_dim={self.hidden_dim}'

            print(LogisticRegression(100, 10).generate())
            print(MultiLayerPerceptron(100, 10, 50).generate())
        elif job_number == '3':
            @machine_learning('K-means', 'DBSCAN')
            @validation_metrics('ARI', 'NMI')
            class Clustering:
                def __init__(self, data):
                    self.data = data

                def generate(self):
                    return f'Clustering model with data={self.data}'

            @machine_learning('PCA', 'TSNE')
            @validation_metrics('ARI', 'Silhouette')
            class DimensionalityReduction:
                def __init__(self, data, output_dim):
                    self.data = data
                    self.output_dim = output_dim

                def generate(self):
                    return f'Dimensionality reduction model with data={self.data} and output_dim={self.output_dim}'

            print(Clustering('data').generate())
            print(DimensionalityReduction('data', 10).generate())
        else:
            print('无效的作业号，请重新输入。')


if __name__ == '__main__':
    main()